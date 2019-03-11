from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor', 'editora', 'isbn', 'numeroPaginas', 'titulo', 'anoPublicacao', 'emailEditora']

def livro_index(request):
    return livro_list(request)

def livro_list(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)

def livro_new(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livro_index')
    return render(request, template_name, {'form': form})

def livro_edit(request, pk, template_name='livro_form.html'):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_index')
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form': form})

def livro_remove(request, pk, template_name='livro_delete.html'):
    livro = Livro.objects.get(pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect('livro_index')
    return render(request, template_name, {'livro': livro})