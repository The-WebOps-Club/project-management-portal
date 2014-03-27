from django.db import models

class UserProfile( model.Model ):

	user = models.ForeignKey( User )
	timestamp = models.DateTimeField( auto_now_add = 'true' )
	description = models.CharField( max_length = 2500)