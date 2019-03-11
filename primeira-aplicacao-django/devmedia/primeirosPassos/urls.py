from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar/', listar),
]

'''
^   para o início do texto
$   para o final do texto
\d  para um dígito
+   para indicar que o item anterior deve ser repetido pelo menos uma vez
()  para capturar parte do padrão
'''
