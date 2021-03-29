from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import post_detail

urlpatterns = [
    url(r'^list/$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),
    url(r'^$', views.post_index, name='index'),
]