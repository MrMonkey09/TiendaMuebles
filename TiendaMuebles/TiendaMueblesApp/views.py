from django.shortcuts import render
from .models import producto, imagen, Comprador, Registro_venta, detalle_Venta
from .functions import handled_uploaded_file

# Create your views here.

def inicio (peticion):
    Productos = producto.objects.filter(Promocionado = True)
    Primer_Producto = Productos.first()
    data = {'productos': Productos, "producto": Primer_Producto
            }
    return render (peticion, 'Inicio.html', data)

def productos (peticion):
    producto_list = imagen.objects.all()
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

def vistaProducto (peticion, id_producto):
    Producto = producto.objects.get(id=id_producto)
    print(Producto)
    data = {
        "titulo": "¡Producto Selecionado!", 
        "producto": Producto
        }
    return render(peticion, 'vistaProducto/vistaProducto.html', data)