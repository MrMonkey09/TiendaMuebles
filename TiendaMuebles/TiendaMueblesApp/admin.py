from django.contrib import admin

from .models import producto, imagen, detalle_Venta, Registro_venta, Comprador
# Register your models here.

class ImagenProducto_Admin(admin.TabularInline):
    model = imagen

class admin_producto(admin.ModelAdmin):
    list_display = ['Nombre_Producto', 'Precio', 'Stock', 'Alto', 'Ancho', 'Largo', 'Fabricado', 'Promocionado']
    search_fields = ['Nombre_Producto']
    search_help_text = "Ingrese el nombre del Producto que desee buscar"
    list_filter = ['Fabricado', 'Promocionado']
    list_editable= ["Fabricado", "Promocionado"]
    inlines = [
        ImagenProducto_Admin
    ]

class admin_imagen(admin.ModelAdmin):
    list_display = ['Ruta']

class admin_Detalle_Venta(admin.ModelAdmin):
    list_display = ['id_registro_Venta', 'Comprador','Email', 'Fecha_Compra','Telefono','id_Producto', 'Comprados', 'Total']
    list_filter = ['id_Producto__Nombre_Producto']
    search_fields = ['id_registro_Venta__id_Comprador__Nombre_Comprador', 'id_registro_Venta__id_Comprador__Email','id_Producto__Nombre_Producto' ]
    search_help_text = "Busque por datos de Comprador o Nombre del producto"

class admin_Venta(admin.ModelAdmin):
    list_display = ['Cantidad_Productos', 'Total', 'Fecha', 'id_Comprador', 'Pagado']
    list_editable = ['Pagado']

class admin_Comprador(admin.ModelAdmin):
    list_display = ['Nombre_Comprador','Email', 'Rut', 'Telefono']
    search_fields = ['Nombre_Comprador']
    search_help_text = "Ingrese el nombre del comprador que desea buscar"
    
admin.site.register(producto, admin_producto)
admin.site.register(imagen, admin_imagen)
admin.site.register(detalle_Venta, admin_Detalle_Venta)
admin.site.register(Registro_venta, admin_Venta)
admin.site.register(Comprador, admin_Comprador)