from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from django.forms.models import modelformset_factory
from agenda.apps.contactos.models import Contacto, Detalle

class ContactoForm(forms.ModelForm):
    """Form for Contacto"""   
    class Meta:
        model = Contacto
        exclude = ('detalle',)

DetalleFormSet = inlineformset_factory(Contacto, Detalle, extra=2, can_delete=False)