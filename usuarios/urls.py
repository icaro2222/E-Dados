
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import logar

urlpatterns = [
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('logar/', logar, name="logar")
]