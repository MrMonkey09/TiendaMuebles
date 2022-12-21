from django import forms
from .models import solicitud_contacto, solicitud_diseño

class SolicitudContactoForm(forms.ModelForm):
    
    class Meta:
        model = solicitud_contacto
        fields = "__all__"
        
class SolicitudDiseñoForm(forms.ModelForm):
    
    class Meta:
        model = solicitud_diseño
        fields = "__all__"