from django import forms
from django.forms.extras.widgets import SelectDateWidget
from finance.models import *
from django.forms.models import modelformset_factory

CHOICES = (('approved', 'approved'), ('disapproved', 'disapproved'),)

class NewAdvanceForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('project', 'amount', 'split_up',)
		widgets = {'project': forms.HiddenInput}

class MentorApprovalForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('is_app_mentor', 'comments', 'project', 'amount', 'split_up',)
		readonly_fields = ('split_up', 'project', 'amount',)
		widgets = {	
			'comments': forms.Textarea(attrs={'cols': 70, 'rows': 3}),
			'project': forms.HiddenInput,
			'split_up': forms.HiddenInput,
			'amount': forms.HiddenInput,
			}

'''	def __init__(self, *args, **kwargs):  
		super(MentorApprovalForm, self).__init__(*args, **kwargs)
		self.fields["is_app_mentor"].choices = CHOICES	'''

MentorApprovalFormset = modelformset_factory(Advance, form=MentorApprovalForm)

class MentorApprovalForm2(forms.ModelForm):

	class Meta:
		model = Reimbursement
		fields = ('project', 'is_app_mentor', 'comments',)
		readonly_fields = ('project', )
		widgets = {
			'project': forms.HiddenInput,
			'comments': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
			'is_app_mentor': forms.Select(attrs={'class':'status_field'}),
		}

'''	def __init__(self, *args, **kwargs):  
		super(MentorApprovalForm2, self).__init__(*args, **kwargs)
		self.fields["is_app_mentor"].choices = CHOICES	'''

MentorApprovalFormset2 = modelformset_factory(Reimbursement, form=MentorApprovalForm2)

class BillForm(forms.ModelForm):

	class Meta:
		model = Bill
		widgets = {'date': SelectDateWidget}

class InstallmentForm(forms.ModelForm):

	class Meta:
		model = Installment
		widgets = {'date': SelectDateWidget}

class CoreApprovalForm(forms.ModelForm):
	
	class Meta:
		model = Advance
		fields = ('project', 'amount', 'split_up', 'is_app_mentor', 'is_app_core', 'due_date', 'comments',)
		readonly_fields = ('project', 'is_app_mentor', 'is_app_core', 'split_up', 'amount',)
		widgets = {
			'project': forms.HiddenInput,
			'amount': forms.HiddenInput,
			'split_up': forms.HiddenInput,
			'is_app_mentor': forms.HiddenInput,
			'due_date': SelectDateWidget,
			'is_app_core': forms.Select(attrs={'class':'status_field'}),
			'comments': forms.Textarea(attrs={'rows':3, 'cols': 40}),
		}

'''	def __init__(self, *args, **kwargs):  
		super(CoreApprovalForm, self).__init__(*args, **kwargs)
		self.fields["is_app_core"].choices = CHOICES  '''

CoreApprovalFormset = modelformset_factory(Advance, form=CoreApprovalForm)	

class CoreApprovedForm(forms.ModelForm):
	
	class Meta:
		model = Advance
		fields = ('project', 'amount', 'split_up', 'is_app_mentor', 'is_app_core', 'due_date', 'comments', 'installments')
		widgets = {
			'project': forms.HiddenInput,
			'amount': forms.HiddenInput,
			'split_up': forms.HiddenInput,
			'is_app_mentor': forms.HiddenInput,
			'due_date': SelectDateWidget,
			'is_app_core': forms.HiddenInput,
			'comments': forms.Textarea(attrs={'rows':3, 'cols': 40}),
		}

CoreApprovedFormset = modelformset_factory(Advance, form=CoreApprovedForm)	