from django.shortcuts import render
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
import re
# simple seearch view that accepts a search value and looks for it in the data rendered by data_view
"""
def get_match_count( term, data ):
	res = 0
	for i in data.split(' '):
		if term.lower() == i.lower():
			res+=1
	return res

def simple_search( request, *args, **kwargs ):

	term = kwargs['search']
	obj_list = []
	for s_model in settings.SEARCH_MODELS:
		for obj in s_model['model'].objects.all():
			data =  s_model['data_view'](obj)
			obj.weight = 0
			for i in data:
				obj.weight = get_match_count( term, data[i] )
				obj_list.append([obj,s_model['view']])

	obj_list.sort( key = lambda u:u[0].weight )
	obj_list.reverse()
	return obj_list[:10]"""