#!/usr/bin/python
# -*- coding: utf-8 -*-

from project.models import Club
from django.contrib.auth.models import User
from project.permissions import PermissionHandler

def site_url(request):
    """
        This is the context processor for templates to provide the base url of the site
    """
    from django.conf import settings
    return {'site_url': settings.SITE_URL}

def static_url(request):
    """
        This is the context processor for templates to provide the static url of the site
    """
    from django.conf import settings
    return {'static_url': settings.STATIC_URL}

def global_context(request):
    # provide context data for the leftbar.
    ctx = {'club_list': Club.objects.all(), 'all_users':User.objects.all()}
    if request.user.is_authenticated() and PermissionHandler.create_club( request.user ):
        ctx['allow_club_create'] = 1
    else:
        ctx['allow_club_create'] = 0
    
    return ctx
