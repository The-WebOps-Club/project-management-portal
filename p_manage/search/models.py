from django.db import models

class Tagged:
	tags = models.ManyToManyField( Tag )

class Tag( models.Model ):
	label = models.CharField( max_length = 50 )