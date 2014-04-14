from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.core.urlresolvers import reverse
dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^admin/', include(admin.site.urls)),
    url( r'^account/', include('userprofile.urls')),
    url( r'^$', RedirectView.as_view( url = settings.LOGIN_URL )), # testing base template. to be replaced with index.html soon.
    url( r'^', include('project.urls', namespace = 'project' ) ),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

)
urlpatterns += patterns('django.views.static', (r'^static/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.STATIC_ROOT,
                        'show_indexes': True}))

urlpatterns += patterns('django.views.static', (r'^media/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.MEDIA_ROOT,
                        'show_indexes': True}))