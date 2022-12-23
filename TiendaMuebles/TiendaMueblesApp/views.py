from django.shortcuts import render
from .models import producto, imagen, Comprador, Registro_venta, detalle_Venta
from .functions import handled_uploaded_file

# Create your views here.

def inicio (peticion):
    promocionados = []
    imagen_list = imagen.objects.all()
    for image in imagen_list:
        if image.Id_Producto.Promocionado:
            if image in promocionados:
                pass
            else:
                promocionados.append(image)
                print("producto"+image.Id_Producto.Nombre_Producto+" promocionado")
    
    data = {"titulo": "Inicio", "productos": promocionados}
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

def vistaProducto (peticion):
    data = {"titulo": "¡Producto Selecionado!"}
    return render(peticion, 'vistaProducto/vistaProducto.html', data)