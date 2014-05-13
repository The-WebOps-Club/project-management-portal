from django.db import models
from project.models import Project

STATUS = (('approved', 'approved'), ('disapproved', 'disapproved'), ('pending', 'pending'),)

class Advance(models.Model):

	project = models.ForeignKey(Project)
	applied_date = models.DateField(auto_now_add=True)
	amount = models.FloatField(default=0, max_length=10)
	split_up = models.TextField(null=True)
	is_app_mentor = models.CharField(choices=STATUS, max_length=15)
	is_app_core = models.CharField(choices=STATUS, max_length=15)
	approved_date = models.DateField(null=True)
	received_date = models.DateField(null=True)
	due_date = models.DateField(null=True)
	comments = models.TextField(null=True)

	def __unicode__(self):
		return str(self.project)+'--'+str(self.applied_date)

class Reimbursement(models.Model):

	project = models.ForeignKey(Project)
	is_app_mentor = models.CharField(choices=STATUS, max_length=15)
	is_app_core = models.CharField(choices=STATUS, max_length=15)
	applied_date = models.DateField(auto_now_add=True)
	received_date = models.DateField(null=True)
	received = models.FloatField(max_length=10, default=0)

	def amount(self):
		total = 0
		bills = Bill.objects.filter(project=self.project)
		for bill in bills:
			total+= bill.amount
		return total

	def is_paid(self):
		if self.amount == self.received:
			return True
		else:
			return False

	def __unicode__(self):
		return str(self.project)+'--'+str(self.applied_date)

class Bill(models.Model):
	project = models.ForeignKey(Project)
	shop = models.CharField(max_length=40)
	number = models.CharField(max_length=20)
	amount = models.FloatField(max_length=10, default=0)
	date = models.DateField(default=None)
	advance = models.ForeignKey(Advance)
	reimb = models.ForeignKey(Reimbursement)
	image = models.ImageField(upload_to='finance/bills')

	def __unicode__(self):
		return str(self.shop)+'--'+str(self.number)
