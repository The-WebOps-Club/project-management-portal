from django import forms
from django.forms.extras.widgets import SelectDateWidget
from finance.models import *


class NewAdvanceForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('project', 'amount', 'split_up',)
		widgets = {'project': forms.HiddenInput}

class MentorApprovalForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('is_app_mentor', 'comments',)
		readonly_fields = ('project', 'applied_date', 'amount', 'split_up',)

class BillForm(forms.ModelForm):

	class Meta:
		model = Bill
		widgets = {'date': SelectDateWidget}

class InstallmentForm(forms.ModelForm):

	class Meta:
		model = Installment
		widgets = {'date': SelectDateWidget}
		