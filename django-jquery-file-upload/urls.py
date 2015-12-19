from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', lambda x: HttpResponseRedirect('/upload/new/')),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

from os.path import join, abspath, dirname
urlpatterns += [
    url(r'^media/(.*)$', serve, {'document_root': join(abspath(dirname(__file__)), 'media')}),
]
