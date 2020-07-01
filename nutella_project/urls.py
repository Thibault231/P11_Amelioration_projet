"""nutella_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from food_selector import views


urlpatterns = [
    url(
     r'^$',
     views.index, name='index'),
    url(
     r'^accounts/',
     include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(
     r'^food_selector/',
     include(('food_selector.urls', 'food_selector'), namespace='food_selector')),
    url(
    r'^save_favorite/',
    include(('save_favorite.urls', 'save_favorite'), namespace='save_favorite')),
    url(
     r'^admin/',
     admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
