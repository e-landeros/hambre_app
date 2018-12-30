"""hambre_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from hambreApp import views
# dont need auth_views 
# from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home, name='home'),
#     path('restaurant/sign-in/', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'),
#     name= 'restaurant-sign-in'),
#     path('restaurant/sign-out/', auth_views.LogoutView {'next_page': '/'},
#     name = 'restaurant-sign-out'),
#     path('restaurant/', views.restaurant_home, name = 'restaurant-home'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('restaurant/', include('django.contrib.auth.urls')),
    path('restaurant/', views.restaurant_home, name = 'restaurant-home'),
    path('restaurant/register/', views.restaurant_registration, name='resaturant-registration'),
]