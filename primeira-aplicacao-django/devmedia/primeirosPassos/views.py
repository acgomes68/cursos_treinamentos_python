from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def listar(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'lista.html', {'pessoa': pessoa})
