from django.shortcuts import render

# Create your views here.
def inicio (peticion):
    data = {"titulo": "Inicio"}
    return render(peticion, 'inicio.html', data)

def productos (peticion):
    data = {"titulo": "Productos"}
    return render(peticion, 'productos/productos.html', data)

def solicitudDiseño (peticion):
    data = {"titulo": "¡Envianos tus diseños!"}
    return render(peticion, 'solicitudDiseños/solicitudDiseños.html', data)

def seguimiento (peticion):
    data = {"titulo": "Seguimiento"}
    return render(peticion, 'seguimiento/seguimiento.html', data)

def contactanos (peticion):
    data = {"titulo": "Contactanos"}
    return render(peticion, 'contactanos/contactanos.html', data)