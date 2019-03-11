from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^lista_registros/', listar_registros),
    # path(r'^lista_registros/(\d+)/$', listar_registros),
]

'''
^   para o início do texto
$   para o final do texto
\d  para um dígito
+   para indicar que o item anterior deve ser repetido pelo menos uma vez
()  para capturar parte do padrão
'''