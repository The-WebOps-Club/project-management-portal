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

                       url(r'project/(?P<project>\d+)/upload/$',
                           upload_document,
                           name='project_upload'),

                       url(r'project/(?P<project>\d+)/update/add/$',
                           CreateUpdate.as_view(),
                           name='update_create'),

                       url(r'project/(?P<project>\d+)/task/add/$',
                           CreateTask.as_view(),
                           name='task_create'),

                       url(r'club/(?P<club>\d+)/$',
                           club_detail_view,
                           name='club_detail'),

                       url(r'project/(?P<project>\d+)/edit/$',
                           project_update,
                           name='project_update'),

                       url(r'club/(?P<club>\d+)/edit/$',
                           club_update,
                           name='club_update'),
                       
                       url(r'club/create/$',
                           TemplateView.as_view( template_name= 'project/club_create.html' ),
                           name='club_create'),
                       )