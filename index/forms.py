from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    password1=forms.CharField(max_length=12, widget=forms.PasswordInput, label='Clave')
    password2=forms.CharField(max_length=12, widget=forms.PasswordInput, label='Confirmar Clave')

    class Meta:
        model= User
        fields=['nombre','apellido','username','email', 'password1','password2']
        help_texts={k:'' for k in fields}


