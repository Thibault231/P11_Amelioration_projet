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
     r'^account/',
     include(('account.urls', 'account'), namespace='account')),
    url(
     r'^food_selector/',
     include(('food_selector.urls', 'food_selector'), namespace='food_selector')),
    url(
    r'^save_favorite/',
    include(('save_favorite.urls', 'save_favorite'), namespace='save_favorite')),
    url(
     r'^admin/',
     admin.site.urls),

    # urls for changing password
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
     name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
     name='password_change'),

    #urls reseting password
    path('password_reset/',
     auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
     name="password_reset"),
    path('password_reset/done/', 
     auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
     name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
     name="password_reset_confirm"),
    path('reset/done/',
     auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name="password_reset_complete")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
