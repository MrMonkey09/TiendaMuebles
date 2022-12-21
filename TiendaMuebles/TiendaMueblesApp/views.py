from django.shortcuts import render
from .models import producto, solicitud_diseño, venta, producto_promocionado, solicitud_contacto
from .forms import SolicitudContactoForm, SolicitudDiseñoForm

# Create your views here.
def inicio (peticion):
    producto_promo = producto_promocionado.objects.get(id=1)
    producto_promo_list = producto_promocionado.objects.all()
    data = {"titulo": "Inicio",
            "productos": producto_promo_list,
            "productoFav": producto_promo}
    return render(peticion, 'inicio.html', data)

def productos (peticion):
    producto_list = producto.objects.all()
    producto_promo = producto_promocionado.objects.get(id=1)
    data = {"titulo": "Productos",
            "productos": producto_list,
            "productoFav": producto_promo}
    return render(peticion, 'productos/productos.html', data)

def solicitudDiseño (peticion):
    data = {"titulo": "¡Envianos tus diseños!"}
    if peticion.method == 'POST':
        formulario = SolicitudContactoForm(data=peticion.POST)
        if formulario.is_valid():
            formulario.save()
            print("solicitud enviada")
        else:
            data["form"] = formulario
    return render(peticion, 'solicitudDiseños/solicitudDiseños.html', data)

def seguimiento (peticion):
    data = {"titulo": "Seguimiento"}
    return render(peticion, 'seguimiento/seguimiento.html', data)

def contactanos (peticion):
    data = {"titulo": "Contactanos", 
            "form": SolicitudContactoForm()}
    
    if peticion.method == 'POST':
        formulario = SolicitudContactoForm(data=peticion.POST)
        if formulario.is_valid():
            formulario.save()
            print("solicitud enviada")
        else:
            data["form"] = formulario
        
    return render(peticion, 'contactanos/contactanos.html', data)