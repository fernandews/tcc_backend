from django.contrib import admin
from django.urls import path

from app.split_views.RegisterView import RegisterView 
from app.split_views.GeolocationView import GeolocationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('geolocation/', GeolocationView.as_view(), name='geolocation')
]
