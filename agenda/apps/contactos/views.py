from django.shortcuts import render_to_response
from django.template import RequestContext
from agenda.apps.contactos.models import Contacto, Detalle
from agenda.apps.contactos.forms import ContactoForm, DetalleForm

def index_view(request):
    if request.method == "POST":
        contactoform = ContactoForm(request.POST)
        detalleform = DetalleForm(request.POST)
        if contactoform.is_valid() and detalleform.is_valid():
            contactoform.save()
            detalleform.save()            
    else:
        cf = ContactoForm()
        df= DetalleForm()
        ctx = {'cf':cf, 'df':df}
        return render_to_response("index.html", ctx, context_instance=RequestContext(request))