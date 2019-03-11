from django.urls import path
from .views import *

urlpatterns = [
    path('livro_list/', livro_list, name='listar_livros'),
]
