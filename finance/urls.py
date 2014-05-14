from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^project/(?P<project_id>\d+)/advance/$', 'finance.views.project_advance'),
	url(r'^project/(?P<project_id>\d+)/reimbursement/$', 'finance.views.project_reimb'),
	url(r'^project/(?P<project_id>\d+)/bill/$', 'finance.views.project_bills'),
	url(r'^project/(?P<project_id>\d+)/$', 'finance.views.project_info'),

	url(r'^core/advance/$', 'finance.views.core_advance'),
	url(r'^core/reimbursement/$', 'finance.views.core_reimb'),
	url(r'^core/$', 'finance.views.core_home'),

)
