# coding: utf-8
""" Module managing urls of
accounts APP for Django program.
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(
        r'^account_creation/$',
        views.account_creation, name='account_creation'),
]
