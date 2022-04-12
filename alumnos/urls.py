from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('msg/',LogoutView.as_view(template_name='salida_sist.html'),name='msg')
]
