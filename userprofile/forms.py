from django import forms
from userprofile.models import UserProfile

class UserProfileForm(forms.ModelForm):

	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length = 30)

	class Meta:
		model = UserProfile
		exclude = ('user',)
		widgets = {
			'description': forms.Textarea(attrs={'cols': 100, 'rows': 5})
		}

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['first_name', 'last_name', 'ph_num', 'hostel', 'room', 'expertise', 
			'social_media_URL', 'description', 'pic']
