from django.db import models

# Create your models here.

class producto (models.Model):
    Nombre_Producto= models.CharField(max_length=50)
    Precio = models.PositiveIntegerField()
    Stock = models.PositiveIntegerField()
    Alto = models.PositiveIntegerField()
    Ancho = models.PositiveIntegerField()
    Largo = models.PositiveIntegerField()
    Fabricado = models.BooleanField(verbose_name="A pedido")
    Promocionado= models.BooleanField(default=False, verbose_name="Â¿Promocionar?")
    
    def __str__(self):
        return self.Nombre_Producto
    
class imagen (models.Model):
    class Meta:
        verbose_name_plural = "Imagenes"
    Ruta = models.ImageField(upload_to='static/images/productos/')
    Id_Producto = models.ForeignKey(producto ,on_delete=models.CASCADE, related_name="imagenes")
    
    
class Comprador (models.Model):
    class Meta:
        verbose_name = "comprador"
        verbose_name_plural = "Compradores"
    Nombre_Comprador = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Rut = models.CharField(max_length=12)
    
    def __str__(self):
        return self.Nombre_Comprador

class Registro_venta (models.Model):
    class Meta:
        verbose_name = "Registro de venta"
        verbose_name_plural = "Registros de venta"
    Cantidad_Productos = models.PositiveIntegerField("Productos Vendidos")
    Total = models.PositiveIntegerField()
    Fecha = models.DateField(auto_now_add=True)
    Pagado = models.BooleanField(default=False)
    id_Comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, verbose_name="Comprador")
    
    def __str__(self):
        Llave = str(self.pk)
        return Llave
    
class detalle_Venta (models.Model):
    class Meta:
        verbose_name = "detalle de la venta"
        verbose_name_plural = "Detalles de las ventas"
    id_registro_Venta = models.ForeignKey(Registro_venta, on_delete=models.CASCADE)
    id_Producto = models.ForeignKey(producto, on_delete=models.CASCADE, verbose_name="Producto")

    def Comprador(self):
        nom_Comprador = self.id_registro_Venta.id_Comprador.Nombre_Comprador
        return nom_Comprador
    
    def Email(self):
        correo = self.id_registro_Venta.id_Comprador.Email
        return correo
    
    def Fecha_Compra(self):
        Fecha = self.id_registro_Venta.Fecha
        return Fecha
    
    def Telefono(self):
        celu = self.id_registro_Venta.id_Comprador.Telefono
        return celu
    
    def Comprados(self):
        cantidad = self.id_registro_Venta.Cantidad_Productos
        return cantidad
    
    def Total(self):
        Compradas = self.id_registro_Venta.Cantidad_Productos
        Precio = self.id_Producto.Precio
        Total = Compradas * Precio
        return Total
