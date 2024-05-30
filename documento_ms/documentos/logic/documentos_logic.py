from ..models import Documento
from django.shortcuts import get_object_or_404

def get_documentos():
    queryset=Documento.objects.all()
    return (queryset)

def get_documento(documento_id):
    return get_object_or_404(Documento,pk=documento_id)

def create_documento(form):
    documento = form.save()
    documento.save()
    return ()
