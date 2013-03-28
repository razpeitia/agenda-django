from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from agenda.apps.contactos.models import Contacto, Detalle
from agenda.apps.contactos.forms import DetalleFormSet, ContactoForm

def home(request):
    data = {}
    data['contact_list'] = Contacto.objects.all()
    return render_to_response("index.html", data, context_instance=RequestContext(request))

def add(request, contact_id=None):
    contacto = None
    if contact_id:
        contacto = get_object_or_404(Contacto, pk=contact_id)

    if request.method == "POST":
        contactoform = ContactoForm(request.POST, prefix='contacto', instance=contacto)
        formset = DetalleFormSet(request.POST, prefix='detalle', instance=contactoform.instance)
        if contactoform.is_valid() and formset.is_valid():
            contactoform.save()
            formset.save()
            return redirect('home')
    else:
        contactoform = ContactoForm(prefix='contacto', instance=contacto)
        formset = DetalleFormSet(prefix='detalle', instance=contacto)
    ctx = {'contactoform': contactoform, 'formset': formset}
    return render_to_response("agregar_o_modificar.html", ctx, context_instance=RequestContext(request))

def delete(request, contact_id=None):
    contacto = None
    if contact_id:
        contacto = get_object_or_404(Contacto, pk=contact_id)
    if contacto and request.method == 'POST':
        contacto.delete()
    return redirect('home')