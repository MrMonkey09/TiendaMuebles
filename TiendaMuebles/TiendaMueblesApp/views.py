from django.shortcuts import render, redirect
from .models import producto, imagen, Comprador, Registro_venta, detalle_Venta
from .functions import handled_uploaded_file
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import random

# Create your views here.


def inicio(peticion):
    Productos = producto.objects.filter(Promocionado=True)
    Primer_Producto = Productos.first()
    data = {'productos': Productos, "producto": Primer_Producto
            }
    return render(peticion, 'Inicio.html', data)


def productos(peticion):
    producto_list = producto.objects.all()
    producto_list_promo = producto.objects.filter(Promocionado=True)
    producto_promo = random.choice(producto_list_promo)
    if 'search' in peticion.POST:
        if peticion.POST['search'] != "":
            print(peticion.POST['search'])
            producto_list = producto.objects.filter(
                Nombre_Producto__icontains=peticion.POST['search'])
    data = {"titulo": "Productos",
            "productos": producto_list, "productoPromo": producto_promo}
    return render(peticion, 'productos/productos.html', data)


def solicitudDiseño(peticion):
    data = {"titulo": "¡Envianos tus diseños!"}
    print(peticion.POST)
    
    if peticion.method == 'POST':
        qd = peticion.POST
        
        Nombre_Comprador = qd['nombre']
        Telefono = qd['numeroContacto']
        Email = qd['correo']
        Rut = qd['rut']
        comprador = Comprador(Nombre_Comprador=Nombre_Comprador, Telefono=Telefono,Email=Email, Rut=Rut)
        comprador.save()
        print(comprador)
        
        Nombre_Producto = qd['Nombre_Producto']
        Alto = qd['Alto']
        Ancho = qd['Ancho']
        Largo = qd['Largo']
        solicitud = producto(Nombre_Producto=Nombre_Producto,Precio=0, Stock=0, Alto=Alto, Ancho=Ancho, Largo=Largo, Fabricado=True)
        solicitud.save()
        print(solicitud)
        
        files = peticion.FILES.getlist('file')
        for f in files:
            nuevaImagen = imagen(Ruta=f, Id_Producto=solicitud)
            nuevaImagen.save()

        Cantidad_Productos = qd['Cantidad_Producto']
        nuevaVenta = Registro_venta(Cantidad_Productos=Cantidad_Productos, Total=0, id_Comprador=comprador)
        nuevaVenta.save()
        print(nuevaVenta)
        
        nuevoDetalle = detalle_Venta(id_registro_Venta=nuevaVenta, id_Producto=solicitud)
        nuevoDetalle.save()

    return render(peticion, 'solicitudDiseños/solicitudDiseños.html', data)


def seguimiento(peticion):
    pedido = ""
    if 'search' in peticion.POST:
        if peticion.POST['search'] != "":
            print(peticion.POST['search'])
            pedido = detalle_Venta.objects.get(
                id=peticion.POST['search'])
            print(pedido)
    data = {"titulo": "Seguimiento", "pedido":pedido}
    return render(peticion, 'seguimiento/seguimiento.html', data)


def Contactanos(request):
        if request.method == "POST":
                Nombre_Apellido = request.post["Nombre_Apellido"]
                Telefono = request.post=["Telefono"]
                Correo = request.post=["Correo"]
                Asunto = request.POST['Asunto']
                Mensaje = request.POST['Mensaje']
                
                data = {'Nombre_Apellido' : Nombre_Apellido,
                        'Telefono': Telefono,
                        'Correo': Correo,
                        'Mensaje':Mensaje
                        }
                template = render_to_string('CorreoFormato.html', data)
                
                send_mail(
                        Asunto,
                        '',
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        html_message= template
                )
                return redirect('/')
        return render (request, 'contactanos.html')



def vistaProducto(peticion, id_producto):
    Producto = producto.objects.get(id=id_producto)
    print(Producto)
    data = {
        "titulo": "¡Producto Selecionado!",
        "producto": Producto
    }
    return render(peticion, 'vistaProducto/vistaProducto.html', data)
