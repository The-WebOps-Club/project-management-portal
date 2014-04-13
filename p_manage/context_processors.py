#!/usr/bin/python
# -*- coding: utf-8 -*-

from project.models import Club
from  import User

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
    # provide context data on clubs for the leftbar.
    return {'club_list': Club.objects.all(), 'all_users':User.objects.all()}
