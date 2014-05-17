from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^project/(?P<project_id>\d+)/advance/$', 'finance.views.project_advance', name='project_advance'),
	url(r'^project/(?P<project_id>\d+)/reimbursement/$', 'finance.views.project_reimb', name='project_reimbursement'),
	url(r'^project/(?P<project_id>\d+)/reimbursement/(?P<col_id>\d*)/$', 'finance.views.project_reimb', name='project_reimbursement_2'),
	url(r'^project/(?P<project_id>\d+)/reimbursement/(?P<col_id>\d+)/save/$', 'finance.views.project_reimb_save', name='project_reimbursement_save'),
	url(r'^project/(?P<project_id>\d+)/bill/(?P<objects>[a-z]+)/(?P<object_id>\d+)/$', 'finance.views.project_bills', name='project_bill'),
	url(r'^project/(?P<project_id>\d+)/$', 'finance.views.project_info', name='project_info'),

	url(r'^core/advance/$', 'finance.views.core_advance', name='core_advance'),
	url(r'^core/reimbursement/$', 'finance.views.core_reimb', name='core_reimbursement'),
	url(r'^core/$', 'finance.views.core_home', name='core_home'),

)
