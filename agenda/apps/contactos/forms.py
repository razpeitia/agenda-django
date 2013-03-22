from django.forms import ModelForm
from django import forms
from agenda.apps.contactos.models import *

class ContactoForm(forms.ModelForm):
    """Form for Contacto"""   
    class Meta:
        model = Contacto
        exclude = {'detalle'}
        
class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
