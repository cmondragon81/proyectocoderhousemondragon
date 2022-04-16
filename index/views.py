from django.db import reset_queries
from django.shortcuts import redirect, render
from django.contrib.auth import login as django_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormularioRegistro
from django.contrib.auth.models import User

#------ingreso al sistema login de usuario ---------------------------------------------------
def index(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                nombre=username
                persona=user.first_name + ' ' + user.last_name
                django_login(request, user=user)
                
                if nombre == 'admin':
                    return render(request,'salida_sist.html',{'msj':'Entrada incorrecta del administrador'})
                else:
                    return render(request, 'alumnos/home.html',{'nombre':persona})
            else:
                return render(request,'salida_sist.html',{'msj':'Usuario inexistente'})

        else:
            return render(request,'salida_sist.html',{'msj':'Error de autenticacion'})
    else:
        form=AuthenticationForm()
        return render (request, 'index.html', {'form':form, 'msj':''})

#------registro de usuario en el sistema -----------------------------------------------------
def registrar(request):

    if request.method =='POST':
        form=FormularioRegistro(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            emailuser=form.cleaned_data['email']
            nomusuario=form.cleaned_data['nombre']
            apellidousu=form.cleaned_data['apellido']
            passwordusu=form.cleaned_data['password1']

            user = User.objects.create_user(username,emailuser,passwordusu)
            user.first_name=nomusuario
            user.last_name=apellidousu

            user.save()
            return render(request,'salida_sist.html',{'msj':'Usuario Creado'})


    form=FormularioRegistro()
    return render(request,'registrar.html',{'form':form, 'msj':''})
