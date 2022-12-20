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
    
class imagen (models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    Ruta = models.ImageField(upload_to='static/images/')

class Archivo_Complementario (models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    Ruta = models.ImageField(upload_to='static/images/')
    

class venta (models.Model):
    id_Producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    Cantidad_Productos = models.PositiveIntegerField()
    Total = models.PositiveIntegerField()
    Fecha = models.DateField(auto_now=False, auto_now_add=False)
    
class admin (models.Model):
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=20)
    
class usuario (models.Model):
    Nombre_usuario = models.CharField(max_length=50)
    Rut = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    id_venta = models.ForeignKey(venta, on_delete=models.CASCADE)
    id_Producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    
class producto_promocionado (models.Model):
    id_imagen = models.ForeignKey(imagen, on_delete=models.CASCADE)