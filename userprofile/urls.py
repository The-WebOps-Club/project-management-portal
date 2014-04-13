from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^test/', 'userprofile.views.test'),
	url(r'^$', 'userprofile.views.account'),

)