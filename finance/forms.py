from django import forms
from django.forms.extras.widgets import SelectDateWidget
from finance.models import *
from django.forms.models import modelformset_factory

CHOICES = (('approve', 'approved'), ('disapprove', 'disapproved'),)

class NewAdvanceForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('project', 'amount', 'split_up',)
		widgets = {'project': forms.HiddenInput}

class MentorApprovalForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('is_app_mentor', 'comments', 'project', 'amount', 'split_up',)
		readonly_fields = ('split_up', 'project', 'amount')
		widgets = {	
			'comments': forms.Textarea(attrs={'cols': 70, 'rows': 3}),
			'project': forms.HiddenInput,
			'split_up': forms.HiddenInput,
			'amount': forms.HiddenInput,
			}

MentorApprovalFormset = modelformset_factory(Advance, form=MentorApprovalForm)

class MentorApprovalForm2(forms.ModelForm):

	class Meta:
		model = Reimbursement
		fields = ('project', 'is_app_mentor', 'comments',)
		readonly_fields = ('project', )
		widgets = {
			'project': forms.HiddenInput,
			'comments': forms.Textarea(attrs={'cols': 70, 'rows': 3}),
		}

MentorApprovalFormset2 = modelformset_factory(Reimbursement, form=MentorApprovalForm2)

class BillForm(forms.ModelForm):

	class Meta:
		model = Bill
		widgets = {'date': SelectDateWidget}

class InstallmentForm(forms.ModelForm):

	class Meta:
		model = Installment
		widgets = {'date': SelectDateWidget}		