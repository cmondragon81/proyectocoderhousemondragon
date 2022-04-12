from django.urls import path
from .views import index, registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('msg/',LogoutView.as_view(template_name='salida_sist.html'),name='msg'),
    path('registrar/',registrar,name='registrar')
]
