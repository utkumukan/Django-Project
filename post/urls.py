from django.conf.urls import url
from .views import *

app_name = "post"

urlpatterns = [

    #Sabit URL'ler

    url(r'^index/$', post_index, name="index"),
    url(r'^create/$', post_create, name="create"),

    #Dinamik URL'ler

    #url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    #url(r'^(?P<id>\d+)/update/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
    #url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),

]
