
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .views import logar

urlpatterns = [
    path('logar/', TemplateView.as_view(template_name="login.html"), name='logar'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="login"),
    path('logout/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="logout"),

]