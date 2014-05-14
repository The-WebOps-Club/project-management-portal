from django.db import models
from django.contrib.auth.models import User

class UserProfile( models.Model ):

	user = models.ForeignKey( User )
	description = models.TextField( max_length = 2500, null=True, blank=True)
	ph_num = models.CharField( max_length = 13)
	hostel = models.CharField( max_length = 30)
	room = models.CharField( max_length = 4)
	expertise = models.CharField( max_length = 2500, null=True, blank=True)
	social_media_URL = models.CharField( max_length = 500, null=True, blank=True)
	pic = models.ImageField( upload_to = 'user_pics/', default = 'user_pics/default.jpg')
	is_finance_core = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username

	def is_member(self, project):
		if self.user in project.users.all():
			return True
		else:
			return False

	def is_mentor(self, project):
		if self.user in project.mentors.all():
			return True
		else:
			return False

	def is_in(self, project):
		if self.is_mentor(project) or self.is_member(project):
			return True
		else:
			return False
