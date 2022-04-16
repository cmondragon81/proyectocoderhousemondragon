from django import forms

class MateriasAnotado(forms.Form):
    nombremateria = forms.CharField(label='Nombre de la materia', max_length=30)
    nombreprofesor = forms.CharField(label = 'Profesor a cargo', max_length=30)
