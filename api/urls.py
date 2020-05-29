from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.users_api_view, name="user_view"),
]
