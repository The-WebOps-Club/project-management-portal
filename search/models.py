from django.db import models

class Tag( models.Model ):
	label = models.CharField( max_length = 50 )

	def __unicode__( self ):
		return self.label
	
class Tagged:
	tags = models.ManyToManyField( Tag )
