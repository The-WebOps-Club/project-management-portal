from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from userprofile.models import UserProfile
from userprofile.forms import UserProfileForm
from django.template.loader import render_to_string
from django.template.context import RequestContext
from dajaxice.utils import deserialize_form
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from project.permissions import PermissionHandler
from project.models import *
from project.views import *

@dajaxice_register
def create_blank_project( request, **kwargs):
	if( not PermissionHandler.create_project(request.user, **kwargs ) ): # check for permission using the permissions module.
		raise PermissionDenied( 'You do NOT have permission to create a project :P' )

	project = Project()
	project.desc = 'Detailed Writeup'
	project.brief = 'Brief Writeup'
	project.status = 'Sample Status'
	project.name = 'Sample Name'
	project.club = get_object_or_404( Club, pk = kwargs['club'])
	project.save()

	dajax = Dajax()
	dajax.script('window.location=\''+reverse('project:project_detail', args=[project.pk])+'\'')
	return dajax.json()

@dajaxice_register
def add_core_to_club( request, **kwargs):
	#if( not PermissionHandler.add_cores_to_club(request.user, **kwargs ) ): # check for permission using the permissions module.
	#	raise PermissionDenied( 'You do NOT have permission to add cores :P' )

	#import pdb;pdb.set_trace()
	club = get_object_or_404( Club, pk = kwargs['club'] )
	core_list = kwargs['convenors']
	for core_id in core_list:
		core = get_object_or_404( User, pk=core_id )
		if not core in club.cores.all():
			club.cores.add(core)

	club.save()

	dajax = Dajax()
	dajax.alert('successfully added '+format(len(kwargs['convenors'])))
	return dajax.json()

@dajaxice_register
def add_user_to_project( request, **kwargs):
	#if( not PermissionHandler.add_cores_to_club(request.user, **kwargs ) ): # check for permission using the permissions module.
	#	raise PermissionDenied( 'You do NOT have permission to add cores :P' )

	#import pdb;pdb.set_trace()
	project = get_object_or_404( Project, pk = kwargs['project'] )
	user_list = kwargs['users']
	for user_id in user_list:
		user = get_object_or_404( User, pk=user_id )
		if not user in project.users.all():
			project.users.add(user)

	project.save()

	dajax = Dajax()
	dajax.alert('successfully added '+format(len(kwargs['users']))+ ' users')
	return dajax.json()

@dajaxice_register
def add_mentor_to_project( request, **kwargs):
	#if( not PermissionHandler.add_cores_to_club(request.user, **kwargs ) ): # check for permission using the permissions module.
	#	raise PermissionDenied( 'You do NOT have permission to add cores :P' )

	#import pdb;pdb.set_trace()
	project = get_object_or_404( Project, pk = kwargs['project'] )
	mentor_list = kwargs['mentors']
	for mentor_id in mentor_list:
		mentor = get_object_or_404( User, pk=mentor_id )
		if not mentor in project.mentors.all():
			project.mentors.add(mentor)

	project.save()

	dajax = Dajax()
	dajax.alert('Successfully added '+format(len(kwargs['mentors']))+ ' mentors')
	return dajax.json()

@dajaxice_register
def create_blank_club( request, **kwargs):
	if( not PermissionHandler.create_club(request.user, **kwargs ) ): # check for permission using the permissions module.
		raise PermissionDenied( 'You do NOT have permission to create a club :P' )

	club = Club()
	club.description = 'Detailed Writeup'
	club.name = 'Sample Name'
	club.save()

	dajax = Dajax()
	#dajax.script('window.location=\'http://localhost:8000/club/'+format(club.pk)+'/\'')
	dajax.script('window.location=\''+reverse('project:club_detail',args=[club.pk])+'\'')
	return dajax.json()

@dajaxice_register
def delete_document( request, **kwargs ):

	doc = get_object_or_404( Document, pk = kwargs['doc'] )

	if( (not PermissionHandler.delete_document(request.user, **kwargs )) ): # check for permission using the permissions module.
		raise PermissionDenied( 'You do NOT have permission to create a club :P' )

	doc.delete()

	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()

@dajaxice_register
def comment_on_update( request, **kwargs ):

	if( (not PermissionHandler.create_comment(request.user, **kwargs )) ): # check for permission using the permissions module.
		raise PermissionDenied( 'You do NOT have permission to make comments :P' )

	comment = Comment( user = request.user, content = kwargs['content'] )
	comment.save()

	update = get_object_or_404( Update, pk = kwargs['update'] )
	update.comments.add(comment)
	update.save()


	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()

@dajaxice_register
def comment_on_task( request, **kwargs ):

	if( (not PermissionHandler.create_comment(request.user, **kwargs )) ): # check for permission using the permissions module.
		raise PermissionDenied( 'You do NOT have permission to make comments :P' )

	comment = Comment( user = request.user, content = kwargs['content'] )
	comment.save()

	task = get_object_or_404( Task, pk = kwargs['task'] )
	task.comments.add(comment)
	task.save()


	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()

@dajaxice_register
def delete_update( request, **kwargs ):

	update = get_object_or_404( Update, pk = kwargs['update'] )

	if( (not PermissionHandler.delete_update(request.user, **kwargs )) ): # check for permission using the permissions module.
		dajax = Dajax()
		dajax.alert('You do NOT have this permission')
		return dajax.json()

	update.delete()

	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()

@dajaxice_register
def delete_task( request, **kwargs ):

	task = get_object_or_404( Task, pk = kwargs['task'] )

	if( (not PermissionHandler.delete_task(request.user, **kwargs )) ): # check for permission using the permissions module.
		dajax = Dajax()
		dajax.alert('You do NOT have this permission')
		return dajax.json()

	task.delete()

	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()

@dajaxice_register
def delete_comment( request, **kwargs ):

	comment = get_object_or_404( Comment, pk = kwargs['comment'] )

	if( (not PermissionHandler.delete_comment(request.user, **kwargs )) ): # check for permission using the permissions module.
		dajax = Dajax()
		dajax.alert('You do NOT have this permission')
		return dajax.json()

	for update in Update.objects.filter( comments__in = [comment] ):
		update.commments.remove(comment)

	for task in Task.objects.filter( comments__in = [comment] ):
		task.commments.remove(comment)

	comment.delete()

	dajax = Dajax()
	dajax.script('location.reload(true)')
	return dajax.json()