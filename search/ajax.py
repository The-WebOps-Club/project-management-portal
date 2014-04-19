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
"""
search_instance_index = []


def update_index( request, *args, **kwargs ):
	# search titles and brief descriptions for ties to the search term
	search_for = kwargs['search']
	search_instance_index = []

	class SearchInstance:
		classpath = ''
		instance = None
		datasets = {}
		def __init__(self,classpath='',instance=None):
			self.classpath = classpath
			self.instance = instance
			

	for s in SEARCH_MODELS:
		for obj in s['model'].objects.all():
			i = SearchInstance(classpath = s['classpath'],instance = obj)
			i.datasets = obj.get_search_dataset()
			search_instance_index.append()

def simple_search( request, *args, **kwargs ):

	obj_list = []
	for s_model in settings.SEARCH_MODELS:
		for obj in s_model['model'].objects.all():
			data =  obj.get_search_dataset()
			for i in data:
				obj.weight = get_match_count(data[i])
				obj_list.append([obj,s_model['view']])

	obj_list.sort( key = lambda u:u[0].weight )
	obj_list.reverse()
	return obj_list[:10]"""