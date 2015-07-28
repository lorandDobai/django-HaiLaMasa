"""HaiLaMasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from visitor import views as visitor_views
from organizer import views as organizer_views
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', visitor_views.hello,name = 'home'),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login/auth$',organizer_views.login_auth),
    url(r'^oras/(?P<city>[a-zA-Z]+)?$',visitor_views.city_view),
    url(r'^logout$', organizer_views.logout_view),
    url(r'^dashboard/$',organizer_views.resto_selection, name='resto-list'),
    url(r'^dashboard/restaurant/(?P<pk>[0-9]+)?$', organizer_views.resto_edit, name='resto-edit'),
    url(r'^dashboard/restaurant/\d+/menu/$', organizer_views.menu_data, name='menu-data'),
    url(r'^dashboard/restaurant/validate$',organizer_views.resto_validate,name='resto-valid'),
    url(r'^dashboard/restaurant/(?P<pk>[0-9]+)?/upload$', organizer_views.upload_img, name='upload-img'),
    url(r'^dashboard/restaurant/(?P<pk>[0-9]+)?/delete$', organizer_views.delete_img, name='delete-img'),
    url(r'^restaurant/(?P<pk>[0-9]+)?$',visitor_views.restaurant_view, name='restaurant'),
    url(r'^restaurante/(?P<city>[a-zA-Z]+)?$',visitor_views.restaurants_view)
]
