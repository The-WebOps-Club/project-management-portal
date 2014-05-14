from django import forms
from finance.models import *


class NewAdvanceForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('amount', 'split_up',)
		readonly_fields = ('project',)

class MentorApprovalForm(forms.ModelForm):

	class Meta:
		model = Advance
		fields = ('is_app_mentor', 'comments',)
		readonly_fields = ('project', 'applied_date', 'amount', 'split_up',)
		