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

	if( (not PermissionHandler.delete_document(request.user, **kwargs )) and (not request.user==doc.user) ): # check for permission using the permissions module.
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


