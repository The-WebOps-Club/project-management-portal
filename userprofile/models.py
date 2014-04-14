from django.db import models
from django.contrib.auth.models import User

class UserProfile( models.Model ):

	user = models.ForeignKey( User )
	description = models.TextField( max_length = 2500)
	ph_num = models.CharField( max_length = 13)
	hostel = models.CharField( max_length = 30)
	room = models.CharField( max_length = 4)
	expertise = models.CharField( max_length = 2500)
	social_media_URL = models.CharField( max_length = 500)
	pic = models.ImageField( upload_to = 'user_pics/', default = 'user_pics/default.jpg')

	def __unicode__(self):
		return self.user.username
