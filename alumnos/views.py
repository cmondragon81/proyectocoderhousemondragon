from django.shortcuts import render, redirect
from .forms import MateriasAnotado
from .models import Materias
from django.contrib.auth.models import User

# Create your views here.

# def materias(request):

    # if request.method =='POST':
    #     form=MateriasAnotado(request.POST)
        
    #     if form.is_valid():
    #         datos=form.cleaned_data
    #         guardar=Materias(
    #             nombre=datos['nombremateria'],
    #             profesor=datos['nombreprofesor']
    #         )
    #         guardar.save()
    #         return redirect('materias')
            
    # form=MateriasAnotado
    # return render (request, 'home.html', {'form':form})

def materias(request):
    form=()
    return render (request, 'alumnos/materias.html', {'form':form})