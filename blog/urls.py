from django.contrib import admin
from django.urls import path,include,re_path

from .import views
app_name='blog'
urlpatterns = [

    path('index/',views.index,name="index"),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    re_path(r'^edit/action/$', views.edit_action,name="edit_action"),
    re_path(r'^blog_show/$',views.blog_show,name="blog_show"),
    re_path(r'^blog_single/(?P<article_id>[0-9]+)$',views.blog_single,name="blog_single"),
    re_path(r'^contact/$',views.contact,name="contact"),
    re_path(r'^hotel/$',views.hotel,name="hotel"),
    re_path(r'^places/$',views.places,name='places'),
    re_path(r'^about/$',views.about,name='about')
    ]