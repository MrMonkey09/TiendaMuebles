from django.shortcuts import render, redirect
from .models import producto, imagen, Comprador, Registro_venta, detalle_Venta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import random
from django.core.paginator import Paginator
from TiendaMueblesApp.forms import Contactanos_Form
# Create your views here.


def inicio(peticion):
    Productos = producto.objects.filter(Promocionado=True)
    Primer_Producto = Productos.first()
    data = {'productos': Productos, "producto": Primer_Producto
            }
    return render(peticion, 'inicio.html', data)


def productos(peticion):
    producto_list_promo = producto.objects.filter(Promocionado=True)
    paginator = Paginator(producto_list_promo, 8)
    Page_Num = peticion.GET.get('page')
    Page_obj = paginator.get_page(Page_Num)
    producto_promo = random.choice(producto_list_promo)
    if 'search' in peticion.POST:
        if peticion.POST['search'] != "":
            print(peticion.POST['search'])
            Page_obj = producto.objects.filter(
                Nombre_Producto__icontains=peticion.POST['search'])
    data = {"titulo": "Productos",
            "productos": Page_obj, 
            "paginator": paginator,
            "productoPromo": producto_promo}
    return render(peticion, 'productos/productos.html', data)


def solicitudDiseño(peticion):
    validacion = True
    error_msg = {}
    print(peticion.POST)

    if peticion.method == 'POST':
        qd = peticion.POST
        Nombre_Comprador = qd['nombre']
        for pos, char in enumerate(Nombre_Comprador):
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "@" or char == "." or char == "-" or char == "_" or char == "{" or char == ",":
                error_msg['NombreVal'] = "Campo Nombre y Apellido: " + \
                    char+" <- no es un caracter"
                validacion = False
                print(error_msg)
                break

        Rut = qd['rut']
        for pos, char in enumerate(Rut):
            if char == "a" or char == "A" or char == "b" or char == "B" or char == "c" or char == "C" or char == "d" or char == "D" or char == "e" or char == "E" or char == "f" or char == "F" or char == "g" or char == "G" or char == "h" or char == "H" or char == "i" or char == "I" or char == "j" or char == "J" or char == "l" or char == "L" or char == "m" or char == "M" or char == "n" or char == "N" or char == "ñ" or char == "Ñ" or char == "o" or char == "O" or char == "p" or char == "P" or char == "q" or char == "Q" or char == "r" or char == "R" or char == "s" or char == "S" or char == "t" or char == "T" or char == "u" or char == "U" or char == "v" or char == "V" or char == "w" or char == "W" or char == "x" or char == "X" or char == "y" or char == "Y" or char == "z" or char == "Z" or char == "@" or char == "-" or char == "_" or char == "{" or char == "," or char == ".":
                error_msg['RutVal'] = "Campo Rut: " + \
                    char+" <- caracter no valido."
                validacion = False
                print(error_msg)
                break

        Nombre_Producto = qd['Nombre_Producto']
        for pos, char in enumerate(Nombre_Producto):
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "@" or char == "." or char == "-" or char == "_" or char == "{" or char == ",":
                error_msg['NombreProductoVal'] = "Campo Nombre Proyecto: " + \
                    char+" <- no es un caracter"
                validacion = False
                print(error_msg)
                break
            
        if validacion:
            print("formulario valido")
            Telefono = qd['numeroContacto']
            Email = qd['correo']
            comprador = Comprador(Nombre_Comprador=Nombre_Comprador,
                                Telefono=Telefono, Email=Email, Rut=Rut)
            comprador.save()
            print(comprador)

        
            Alto = qd['Alto']
            Ancho = qd['Ancho']
            Largo = qd['Largo']
            
                
            solicitud = producto(Nombre_Producto=Nombre_Producto, Precio=0,
                                Stock=0, Alto=Alto, Ancho=Ancho, Largo=Largo, Fabricado=True)
            solicitud.save()
            print(solicitud)

            files = peticion.FILES.getlist('file')
            for f in files:
                nuevaImagen = imagen(Ruta=f, Id_Producto=solicitud)
                nuevaImagen.save()

            Cantidad_Productos = qd['Cantidad_Producto']
            nuevaVenta = Registro_venta(
                Cantidad_Productos=Cantidad_Productos, Total=0, id_Comprador=comprador)
            nuevaVenta.save()
            print(nuevaVenta)

            nuevoDetalle = detalle_Venta(
                id_registro_Venta=nuevaVenta, id_Producto=solicitud)
            nuevoDetalle.save()

    data = {"titulo": "¡Envianos tus diseños!", "error_msg": error_msg}

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
    form = Contactanos_Form()
    data = {
        'form': form
        }
    if request.method == "POST":
        form = Contactanos_Form(request.POST)

        if form.is_valid():
            Nombre_Apellido = form.cleaned_data["Nombre_Apellido"]
            Telefono = form.cleaned_data["Telefono"]
            Correo = form.cleaned_data["Correo"]
            Asunto = form.cleaned_data["Asunto"]
            Mensaje = form.cleaned_data["Mensaje"]
            Mail = {'Nombre_Apellido' : Nombre_Apellido,
                    'Telefono': Telefono,
                    'Correo': Correo,
                    'Mensaje': Mensaje
                    }
            template = render_to_string('CorreoFormato.html', Mail)
            send_mail(Asunto,'',settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER],html_message= template)
            return redirect('/')
        else:
            form = Contactanos_Form()
    return render (request, 'contactanos/contactanos.html', data)

def vistaProducto(peticion, id_producto):
    Producto = producto.objects.get(id=id_producto)
    imagenes = Producto.imagen_set.all()
    print(Producto)
    data = {
        "titulo": "¡Producto Selecionado!",
        "producto": Producto,
        'imagenes': imagenes
    }
    return render(peticion, 'vistaProducto/vistaProducto.html', data)
