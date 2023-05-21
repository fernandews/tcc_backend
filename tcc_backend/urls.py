from django.contrib import admin
from django.urls import path

from app.split_views.RegisterView import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
]
