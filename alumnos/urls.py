from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import materias

urlpatterns = [
    path('msg/',LogoutView.as_view(template_name='salida_sist.html'),name='msg'),
    path('materias/', materias,name='materias')
]