from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied
from project.models import Update, Project, Task, Club
from project.permissions import PermissionHandler



# curently using class-based views for cleaner code.
# one view for creating, editing and deleting an object of a particular type.
# the views are then mixed to develop the full context for a given page.
class CreateUpdate( CreateView ):
	model = Update
	fields = ['title','content']

	def form_valid( self, form ):
		if( not PermissionHandler.create_update( self.request.user, **self.kwargs ) ):
			raise PermissionDenied( 'You do NOT have permission to make an update :P' ) # <--- change this to a more tactful message :)

		form.instance.user = self.request.user
		form.instance.parent = Project.objects.filter( pk = self.kwargs['project'] )[0]
		return super( CreateUpdate, self ).form_valid( form )

class CreateTask( CreateView ):
	model = Task
	fields = ['title','content']

	def form_valid( self, form ):
		if( not PermissionHandler.create_task( self.request.user, **self.kwargs ) ):
			raise PermissionDenied( 'You do NOT have permission to make a task :P' ) 
		form.instance.user = self.request.user
		form.instance.parent = Project.objects.filter( pk = self.kwargs['project'] )[0]
		return super( CreateTask, self ).form_valid( form )

class CreateProject( CreateView ):
	model = Project
	fields = ['name','desc','status','budget']

	def form_valid( self, form ):
		if( not PermissionHandler.create_project(self.request.user, **self.kwargs ) ): # check for permission using the permissions module.
			raise PermissionDenied( 'You do NOT have permission to make a task :P' ) 
		form.instance.club = Club.objects.filter( pk = self.kwargs['club'] )[0]
		return super( CreateProject, self ).form_valid( form )

class CreateClub( CreateView ):
	model = Club
	fields = ['name','description']

	def form_valid( self, form ):
		if( not PermissionHandler.create_club(self.request.user, **self.kwargs ) ): # check for permission using the permissions module.
			raise PermissionDenied( 'You do NOT have permission to make a task :P' ) 
		return super( CreateProject, self ).form_valid( form )

class CreateComment( CreateView ):
	model = Comment
	fields = ['content']

	def form_valid( self, form ):
		if( not PermissionHandler.create_comment(self.request.user, **self.kwargs ) ): # check for permission using the permissions module.
			raise PermissionDenied( 'You do NOT have permission to make a task :P' ) 

		form.instance.user = self.request.user 
		if( self.kwargs['target_model'] == 'Update'):
			Update.objects.filter( pk = self.kwargs['update'] )[0].comments.add( form.instance )
		elif( self.kwargs['target_model'] == 'Task'):
			Task.objects.filter( pk = self.kwargs['task'] )[0].comments.add( form.instance )

		return super( CreateProject, self ).form_valid( form )


class MyProjectsListView( ListView ):
	template_name = 'project/project_list.html'
	context_object_name = 'project_list'
	model = Project

	def get(self, request,*args,**kwargs):
		if not request.user.is_authenticated():				# check for authentication
			return PermissionDenied('You\'re not logged in.')	

	def get_queryset(self, *args,**kwargs):
		qs = super(MyProjectsListView, self).get_queryset(*args,**kwargs)
		qs.filter( users__in = self.request.user )
		return qs

	def get_context_data( self ):
		ctx = super(AllProjectsListView, self).get_context_data()
		ctx['page_title'] = 'My Projects'
		return ctx

class AllProjectsListView( ListView ):
	template_name = 'project/project_list.html'
	context_object_name = 'project_list'
	model = Project
	def get_context_data( self ):
		ctx = super(AllProjectsListView, self).get_context_data()
		ctx['page_title'] = 'All Projects'
		return ctx
