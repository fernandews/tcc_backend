from django.contrib import admin
from django.urls import path

from app.split_views.RegisterView import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', RegisterView.as_view(), name='register-user'),
]
