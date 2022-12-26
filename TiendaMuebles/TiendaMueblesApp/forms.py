from django import forms

class Contactanos_Form(forms.Form):
    Nombre_Apellido = forms.CharField(min_length=10,max_length=50, required=True)
    Telefono = forms.IntegerField(required=True)
    Rut = forms.CharField(max_length=9, required=False)
    Correo = forms.EmailField(max_length=50, min_length=15, required=True)
    Asunto = forms.CharField(max_length=20, required=True)
    Mensaje = forms.CharField(widget=forms.Textarea)
    
    Nombre_Apellido.widget.attrs['class'] = 'form-control'
    Telefono.widget.attrs['class'] = 'form-control'
    Rut.widget.attrs['class'] = 'form-control'
    Correo.widget.attrs['class'] = 'form-control'
    Asunto.widget.attrs['class'] = 'form-control'
    Mensaje.widget.attrs['class'] = 'form-control'