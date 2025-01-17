"""files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path("all_chords/", views.all_chords),
    path("filter/<str:chords>", views.filter_endpoint),
    re_path(r'^filter/(?P<chords>.*)$', views.filter_endpoint),
    path("best_order_to_learn_chords/", views.best_order_to_learn_chords),
    re_path(r'^.*$', views.index),  # Catch-all pattern to serve React app
]