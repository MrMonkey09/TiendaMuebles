from django.db import models

# Create your models here.
class producto (models.Model):
    Nombre_Producto= models.CharField(max_length=50)
    Precio = models.PositiveIntegerField()
    Stock = models.PositiveIntegerField()
    Material = models.CharField(max_length=50)
    Alto = models.PositiveIntegerField()
    Ancho = models.PositiveIntegerField()
    Largo = models.PositiveIntegerField()
    Imagenes = models.FileField(upload_to='static/images/productos/')
    
class diseño (models.Model):
    Nombre_Apellido =  models.CharField(max_length=100, null=False)
    Correo = models.EmailField() 
    Numero_Contacto = models.IntegerField()
    Asunto = models.CharField(max_length=256, null=False)
    Contenido_Mensaje = models.TextField(null=False)
    Archivos_Complementarios = models.FileField(upload_to='static/docs/')

class venta (models.Model):
    Cantidad_Productos = models.PositiveIntegerField()
    Total = models.PositiveIntegerField()
    Fecha = models.DateField(auto_now=False, auto_now_add=False)
    Nombre_usuario = models.CharField(max_length=50)
    Rut = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    id_Producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    
class admin (models.Model):
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=20)
    
class producto_promocionado (models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)

class contacto (models.Model):
    Nombre_Apellido =  models.CharField(max_length=100, null=False)
    Correo = models.EmailField() 
    Numero_Contacto = models.IntegerField()
    Asunto = models.CharField(max_length=256, null=False)
    Contenido_Mensaje = models.TextField(null=False)

class estado (models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE, null=True, blank=True)
    id_diseño = models.ForeignKey(diseño, on_delete=models.CASCADE, null=True, blank=True)
    nombre_estado = models.CharField(max_length=256, null=False, blank=False)