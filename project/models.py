from django.db import models
from search.models import Tagged
from django.contrib.auth.models import User
# shift models to a different app if necessary.
class Document( models.Model, Tagged ):

	name = models.CharField( max_length = 100 )
	desc = models.CharField( max_length = 1000 )
	doc = models.FileField( upload_to = 'filebase' )
	timestamp = models.DateTimeField( auto_now_add = 'true' )

	def __unicode__( self ):
		return self.name

class Club( models.Model ):
	name = models.CharField( max_length = 200 )
	description = models.CharField( max_length = 2500 )
	cores = models.ManyToManyField( User )


class Project( models.Model, Tagged ):

	club = models.ForeignKey( Club , related_name = 'parent_club' )
	name = models.CharField( max_length = 100 )
	desc = models.CharField( max_length = 1000 )
	status = models.CharField( max_length = 1000 )
	users = models.ManyToManyField( User , related_name = 'project_member' )
	mentors = models.ManyToManyField( User, related_name = 'project_mentor' )
	budget = models.CharField( max_length = 10 )
	documents = models.ManyToManyField( Document )

	def __unicode__( self ):
		return self.name

class Comment( models.Model ):
	
	user = models.ForeignKey( User )
	content = models.CharField( max_length = 500 )
	timestamp = models.DateTimeField( auto_now_add = 'true')

	def __unicode__( self ):
		return self.content[:20] + '...'

class Update( models.Model, Tagged ):
	parent = models.ForeignKey( Project )
	user = models.ForeignKey( User, related_name = 'update_creator' )
	title = models.CharField( max_length = 100 )
	content = models.CharField( max_length = 2500 )
	timestamp = models.DateTimeField( auto_now_add = 'true' )
	comments = models.ManyToManyField( Comment )

	def __unicode__( self ):
		return self.title

class Task( models.Model, Tagged ):

	parent = models.ForeignKey( Project )
	user = models.ForeignKey( User, related_name = 'task_creator' )
	title = models.CharField( max_length = 100 )
	content = models.CharField( max_length = 2500 )
	deadline = models.DateTimeField()
	timestamp = models.DateTimeField( auto_now_add = 'true' )
	assigned = models.ManyToManyField( User, related_name = 'task_assigned' )
	percent = models.IntegerField( choices = [(x,x) for x in range(0,101)] )
	comments = models.ManyToManyField( Comment )


	def __unicode__( self ):
		return self.title

