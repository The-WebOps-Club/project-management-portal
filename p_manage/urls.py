from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^admin/', include(admin.site.urls)),
    url( r'^$', TemplateView.as_view( template_name = 'base.html' ) ), # testing base template. to be replaced with index.html soon.
    url( r'^', include('project.urls', namespace = 'project' ) )
)

urlpatterns += patterns('django.views.static', (r'^static/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.STATIC_ROOT,
                        'show_indexes': True}))