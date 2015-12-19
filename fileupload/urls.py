# encoding: utf-8
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^new/$', views.FileCreateView.as_view(), name='upload-new'),
    url(r'^(?P<token_id>[a-z0-9\-]+)$', views.AngularVersionCreateView.as_view(), name='upload-angular'),
    url(r'^(?P<token_id>[a-z0-9\-]+)/delete/(?P<pk>\d+)$', views.FileDeleteView.as_view(), name='upload-delete'),
    url(r'^(?P<token_id>[a-z0-9\-]+)/view/$', views.FileListView.as_view(), name='upload-view'),
]
