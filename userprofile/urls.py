from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
	url(r'^test/', 'userprofile.views.test'),
	url(r'^user/', 'userprofile.views.account'),
	url(r'^upload/', 'userprofile.views.upload'),
	url(r'^password/change/$',
	                auth_views.password_change,
	                name='password_change'),
	  url(r'^password/change/done/$',
	                auth_views.password_change_done,
	                name='password_change_done'),
	  url(r'^password/reset/$',
	                auth_views.password_reset,
	                name='password_reset'),
	  url(r'^password/reset/done/$',
	                auth_views.password_reset_done,
	                name='password_reset_done'),
	  url(r'^password/reset/complete/$',
	                auth_views.password_reset_complete,
	                name='password_reset_complete'),
	  url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
	                auth_views.password_reset_confirm,
	                name='password_reset_confirm'),
	
	url(r'^', include('registration.backends.default.urls')),

)