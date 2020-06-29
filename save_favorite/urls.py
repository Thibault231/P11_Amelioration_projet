# coding: utf-8
""" Module managing urls of
food_selector APP for Django program.
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^history/$', views.history, name='history'),
    url(r'^save/(?P<item_id>[0-9]+)/$', views.save, name='save'),
]