from django.db import models
from django.contrib.auth.models import User
class UserProfile( models.Model ):

	user = models.ForeignKey( User )
	timestamp = models.DateTimeField( auto_now_add = 'true' )
	description = models.CharField( max_length = 2500)