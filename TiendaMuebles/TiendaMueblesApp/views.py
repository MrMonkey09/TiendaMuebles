from django.shortcuts import render
from .models import producto, imagen, Comprador, Registro_venta, detalle_Venta
from .functions import handled_uploaded_file

# Create your views here.

def inicio (peticion):
    data = {"titulo": "Inicio"}
    return render(peticion, 'inicio.html', data)

def productos (peticion):
    producto_list = producto.objects.all()
    data = {"titulo": "Productos",
            "productos": producto_list}
    return render(peticion, 'productos/productos.html', data)

def solicitudDiseño (peticion):
    data = {"titulo": "¡Envianos tus diseños!"}
    if peticion.method == 'POST':
        pass
    
    return render(peticion, 'solicitudDiseños/solicitudDiseños.html', data)

def seguimiento (peticion):
    data = {"titulo": "Seguimiento"}
    return render(peticion, 'seguimiento/seguimiento.html', data)

def contactanos (peticion):
    data = {"titulo": "Contactanos"}
    
    if peticion.method == 'POST':
        pass
        
    return render(peticion, 'contactanos/contactanos.html', data)