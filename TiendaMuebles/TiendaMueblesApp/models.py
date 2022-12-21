from django.db import models

# Create your models here.
class producto (models.Model):
    Nombre_Producto= models.CharField(max_length=50, null=False, blank=False)
    Precio = models.PositiveIntegerField(null=False, blank=False)
    Stock = models.PositiveIntegerField(null=False, blank=False)
    Material = models.CharField(max_length=50, null=False, blank=False)
    Alto = models.PositiveIntegerField(null=False, blank=False)
    Ancho = models.PositiveIntegerField(null=False, blank=False)
    Largo = models.PositiveIntegerField(null=False, blank=False)
    Imagen_1 = models.FileField(upload_to='static/images/productos/')
    Imagen_2 = models.FileField(upload_to='static/images/productos/')
    Imagen_3 = models.FileField(upload_to='static/images/productos/')
    Imagen_4 = models.FileField(upload_to='static/images/productos/')
    
    def __str__(self):
        return self.Nombre_Producto
    
    
class solicitud_diseño (models.Model):
    Nombre_Apellido =  models.CharField(max_length=100, null=False, blank=False)
    Correo = models.EmailField() 
    Numero_Contacto = models.IntegerField(null=False, blank=False)
    Nombre_Proyecto = models.CharField(max_length=256, null=False)
    Material = models.CharField(max_length=50, null=False, blank=False)
    Alto = models.PositiveIntegerField(null=False, blank=False)
    Ancho = models.PositiveIntegerField(null=False, blank=False)
    Largo = models.PositiveIntegerField(null=False, blank=False)
    Descripcion = models.TextField()
    Archivo_Complementario_1 = models.FileField(upload_to='static/docs/')
    Archivo_Complementario_2 = models.FileField(upload_to='static/docs/')
    Archivo_Complementario_3 = models.FileField(upload_to='static/docs/')
    Archivo_Complementario_4 = models.FileField(upload_to='static/docs/')
    
    def __str__(self):
        return self.Nombre_Proyecto

class venta (models.Model):
    Cantidad_Productos = models.PositiveIntegerField()
    Total = models.PositiveIntegerField()
    Fecha = models.DateField(auto_now=False, auto_now_add=False)
    Nombre_cliente = models.CharField(max_length=50,null=False, blank=False)
    Rut = models.CharField(max_length=15,null=False, blank=False)
    Email = models.CharField(max_length=50,null=False, blank=False)
    Telefono = models.CharField(max_length=50,null=False, blank=False)
    Estado = models.CharField(max_length=256)
    id_Producto = models.ForeignKey(producto, on_delete=models.CASCADE, null=True, blank=True)
    id_diseño = models.ForeignKey(solicitud_diseño, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.Nombre_cliente
    
class producto_promocionado (models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE,null=False, blank=False)
    
    def __str__(self):
        return self.id_producto.Nombre_Producto

class solicitud_contacto (models.Model):
    Nombre_Apellido =  models.CharField(max_length=100, null=False)
    Correo = models.EmailField() 
    Numero_Contacto = models.IntegerField()
    Asunto = models.CharField(max_length=256, null=False)
    Contenido_Mensaje = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.Nombre_Apellido