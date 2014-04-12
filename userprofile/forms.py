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


"""	first_name = forms.CharField( max_length = 30)
	last_name = forms.CharField( max_length = 30)
	description = forms.CharField( max_length = 2500)
	ph_num = forms.CharField( max_length = 13)
	hostel = forms.CharField( max_length = 30)
	room = forms.CharField( max_length = 4)
	expertise = forms.CharField( max_length = 2500)
	sm_url = forms.CharField( max_length = 500)
	pic = forms.ImageField( upload_to = 'media/user_pics/')"""
