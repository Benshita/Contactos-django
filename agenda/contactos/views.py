from django.shortcuts import render, get_object_or_404, redirect 
from .models import Contacto
from .forms import ContactoForm

from agenda.contactos import models # Importamos Q para poder hacer consultas las cuales la vamos a usar para hacer busquedas

def lista_contactos(request):
    query = request.GET.get('q', '')
    if query:
        contactos = Contacto.objects.filter(
            models.Q(nombre__icontains=query) | models.Q(correo__icontains=query)
        )
    else:
        contactos = Contacto.objects.all()
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos, 'query': query})

def detalle_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    return render(request, 'contactos/detalle_contacto.html', {'contacto': contacto})

def nuevo_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/nuevo_contacto.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar_contacto.html', {'contacto': contacto})