# encoding: utf-8
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^new/$', views.FileCreateView.as_view(), name='upload-new'),
    url(r'^angular/$', views.AngularVersionCreateView.as_view(), name='upload-angular'),
    url(r'^delete/(?P<pk>\d+)$', views.FileDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', views.FileListView.as_view(), name='upload-view'),
]
