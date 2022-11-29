from django.shortcuts import render

# Create your views here.
def inicio (peticion):
    data = {}
    return render(peticion, 'inicio.html', data)