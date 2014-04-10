"""
 URL Patterns for the Project app.
"""



from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView

#from accounts.views import AccountActivationView as ActivationView
from project.views import *

# the links given below link the three main project pages with their urls.
urlpatterns = patterns('',
                       url(r'project/(?P<project>\d+)/$',
                           project_detail_view,
                           name='project_detail'),

                       url(r'project/self/$',
                           MyProjectsListView.as_view(),
                           name='project_self'),

                       url(r'project/all/$',
                           AllProjectsListView.as_view(),
                           name='project_all'),
                       )
					   
                       