from django.db import models
from project.models import Project

STATUS = (('approved', 'approved'), ('disapproved', 'disapproved'), ('pending', 'pending'),)

class Installment(models.Model):
	amount = models.FloatField(max_length=10)
	date = models.DateField()

	def __unicode__(self):
		return str(self.amount)+'--'+str(self.date)

class Bill(models.Model):

	shop = models.CharField(max_length=40)
	number = models.CharField(max_length=20)
	amount = models.FloatField(max_length=10)
	date = models.DateField(default=None, blank=True, null=True)
	image = models.ImageField(upload_to='finance/bills')

	def __unicode__(self):
		return str(self.shop)+'--'+str(self.number)

class Collection(models.Model):

	bills = models.ManyToManyField(Bill)

	def amount(self):
		total = 0
		for bill in self.bills.all():
			total+= bill.amount
		return total

	def __unicode__(self):
		return 'Collection--'+str(self.id)

class Advance(models.Model):

	project = models.ForeignKey(Project)
	applied_date = models.DateField(auto_now_add=True)
	amount = models.FloatField(max_length=10)
	split_up = models.TextField()
	is_app_mentor = models.CharField(choices=STATUS, max_length=15, default='pending', blank=False)
	is_app_core = models.CharField(choices=STATUS, max_length=15, default='pending', blank=False)
	approved_date = models.DateField(null=True, blank=True)
	due_date = models.DateField(null=True, blank=True)
	comments = models.TextField(null=True, blank=True)
	installments = models.ManyToManyField(Installment, blank=True, null=True)
	bills = models.ManyToManyField(Bill, blank=True, null=True)

	def __unicode__(self):
		return str(self.project)+'--'+str(self.applied_date)+'--'+str(self.amount)

	def received(self):
		total = 0
		for i in self.installments.all():
			total+= i.amount
		return total

	def is_received(self):
		return self.received() != 0

	def remainder(self):
		return self.amount - self.received()

	def ins_as_table(self):
		string = '<table class="table table-striped table-bordered table-condensed id="adv_ins_table">'
		string+= '<tr><th>Date</th><th>Amount</th></tr>'
		for i in self.installments.all():
			string+= '<tr><td>'+str(i.date.strftime('%d %b %Y'))+'</td><td>'+str(i.amount)+'</td></tr>'
		string+= '</table>'
		return string

class Reimbursement(models.Model):

	project = models.ForeignKey(Project)
	is_app_mentor = models.CharField(choices=STATUS, max_length=15, default='pending', blank=False)
	is_app_core = models.CharField(choices=STATUS, max_length=15, default='pending', blank=False)
	applied_date = models.DateField(auto_now_add=True)
	approved_date = models.DateField(null=True, blank=True)
	installments = models.ManyToManyField(Installment, blank=True, null=True)
	bills = models.ManyToManyField(Bill, blank=True, null=True)
	comments = models.TextField(null=True, blank=True)

	def amount(self):
		total = 0
		for bill in self.bills.all():
			total+= bill.amount
		return total

	def received(self):
		total = 0
		for i in self.installments.all():
			total+= i.amount
		return total

	def remainder(self):
		return self.amount() - self.received()

	def status(self):
		if self.is_app_core == 'approved':
			return 'approved'
		elif self.is_app_core == 'disapproved' or self.is_app_mentor == 'disapproved':
			return 'disapproved'
		else:
			return 'pending'

	def __unicode__(self):
		return str(self.project)+'--'+str(self.applied_date)

class BudgetInfo(models.Model):
	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.project.name

	def total_budget(self):
		return float(self.project.budget)

	def util_budget(self):
		reimbs = Reimbursement.objects.filter(project=self.project)
		advances = Advance.objects.filter(project=self.project)
		total = 0
		for r in reimbs:
			if r.is_app_core:
				total+= r.amount()
		for a in advances:
			if a.is_app_core:
				total+= a.amount
		return total

	def rem_budget(self):
		return self.total_budget() - self.util_budget()

	def due(self):
		reimbs = Reimbursement.objects.filter(project=self.project)
		advances = Advance.objects.filter(project=self.project)
		total = 0
		for r in reimbs:
			if r.is_app_core:
				total+= r.remainder()
		for a in advances:
			if a.is_app_core:
				total+= a.remainder()
		return total