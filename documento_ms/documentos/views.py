from django.shortcuts import render
from .logic.documentos_logic import get_documentos, create_documento, get_documento
from .forms import DocumentoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def documento_list(request):
    documentos = get_documentos()
    context={'documentosList':documentos}
    return render(request, 'documentos/documentos.html',context)

def documento_update(request,documento_id):
    documento= get_documento(documento_id)
    if request.method == 'POST':
        form= DocumentoForm(request.POST, instance=documento)
        if form.is_valid():
         create_documento(form) 
         return HttpResponseRedirect(reverse("documentosList"))
        else:
         print(form.errors) 
    else: 

        form= DocumentoForm(instance=documento)
    context={
            'form': form,
    }    
    return render(request,'documentos/update_documento.html',context)

def documento_create(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            create_documento(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created documento')
            return HttpResponseRedirect(reverse('documentosCreate'))
        else:
            print(form.errors)
    else:
       
        form = DocumentoForm()

    context = {
        'form': form,
    }
    return render(request, 'documentos/create_documento.html', context)
