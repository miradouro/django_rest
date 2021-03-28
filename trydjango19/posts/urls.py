from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import post_detail

urlpatterns = [
    url(r'^list/$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^(?P<abc>\d+)/$', post_detail, name='detail'),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
    url(r'^$', views.post_index),
]