from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_api_view, name="user_view"),
    path('<str:pk>', views.users_api_view, name='detail'),
]
