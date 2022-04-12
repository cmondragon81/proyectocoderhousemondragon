from cgitb import html
from re import template
from django.urls import path
from .views import index, home, registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('home/',home,name='home'),
    path('msg/',LogoutView.as_view(template_name='salida_sist.html'),name='msg'),
    path('registrar/',registrar,name='registrar')
]
