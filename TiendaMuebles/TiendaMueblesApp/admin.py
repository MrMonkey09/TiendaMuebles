from django.contrib import admin
from .models import producto,  venta, producto_promocionado, solicitud_contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["Nombre_Producto","Precio","Stock","Material","Alto","Ancho","Largo"]
    search_fields = ["Nombre_Producto"]
    list_filter = ["Material"]
    
class SolicitudDiseñoAdmin(admin.ModelAdmin):
    list_display = ["Nombre_Apellido","Correo","Numero_Contacto","Nombre_Proyecto","Material","Alto","Ancho","Largo"]
    search_fields = ["Nombre_Apellido", "Correo", "Nombre_Proyecto"]
    list_filter = ["Material"]
    
class VentaAdmin(admin.ModelAdmin):
    list_display = ["Estado","Cantidad_Productos","Total","Fecha","Nombre_cliente","Rut","Email","Telefono","id_Producto", "id_diseño"]
    search_fields = ["Nombre_cliente"]
    list_filter = ["Estado"]
    
class ProductoPromocionadoAdmin(admin.ModelAdmin):
    list_display = ["id_producto"]
    
class SolicitudContactoAdmin(admin.ModelAdmin):
    list_display = ["Nombre_Apellido","Correo","Numero_Contacto","Asunto"]
    search_fields = ["Nombre_Apellido", "Asunto"]

admin.site.register(producto, ProductoAdmin)
admin.site.register(venta, VentaAdmin)
admin.site.register(producto_promocionado, ProductoPromocionadoAdmin)
admin.site.register(solicitud_contacto, SolicitudContactoAdmin)