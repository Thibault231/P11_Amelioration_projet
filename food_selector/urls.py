# coding: utf-8
""" Module managing urls of
food_selector APP for Django program.
"""
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^result/$', views.result, name='result'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
    url(r'^legal/$', views.legal, name='legal'),
]
