from django import forms

class Contactanos_Form(forms.Form):
    Nombre_Apellido = forms.CharField(min_length=10,max_length=50, required=True)
    Telefono = forms.IntegerField(required=True)
    Rut = forms.CharField(max_length=9, required=False)
    Correo = forms.EmailField(max_length=50, min_length=15, required=True)
    Asunto = forms.CharField(max_length=20, required=True)
    Mensaje = forms.CharField(widget=forms.Textarea)
    
    Nombre_Apellido.widget.attrs['class'] = 'form-control text-center'
    Telefono.widget.attrs['class'] = 'form-control text-center'
    Rut.widget.attrs['class'] = 'form-control text-center'
    Correo.widget.attrs['class'] = 'form-control text-center'
    Asunto.widget.attrs['class'] = 'form-control text-center'
    Mensaje.widget.attrs['class'] = 'form-control text-center'
    
# class FormularioComprador(forms.Form):
#     Nombre_Comprador = forms.CharField(max_length=100, required=True)
#     Telefono = forms.CharField(max_length=9, required=True)
#     Email = forms.EmailField(max_length=100, required=True)
#     Rut = forms.CharField(max_length=9, required=True)
#     Nombre_Producto = forms.CharField(max_length=100, required=True)
#     Alto = forms.IntegerField(max_value=999, min_value=0, required=True)
#     Ancho = forms.IntegerField(max_value=999, min_value=0, required=True)
#     Largo = forms.IntegerField(max_value=999, min_value=0, required=True)
#     Cantidad_Productos= forms.IntegerField(max_value=10, min_value=1, required=True)
    
#     Nombre_Comprador.widget.attrs['class'] = 'form-control text-center'
#     Telefono.widget.attrs['class'] = 'form-control text-center'
#     Rut.widget.attrs['class'] = 'form-control text-center'
#     Email.widget.attrs['class'] = 'form-control text-center'
#     Nombre_Producto.widget.attrs['class'] = 'form-control text-center'
#     Alto.widget.attrs['class'] = 'form-control text-center'
#     Ancho.widget.attrs['class'] = 'form-control text-center'
#     Largo.widget.attrs['class'] = 'form-control text-center'
#     Cantidad_Productos.widget.attrs['class'] = 'form-control text-center'