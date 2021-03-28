from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^list/$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^detail/$', views.post_detail),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
    url(r'^$', views.post_index),
]