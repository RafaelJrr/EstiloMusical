from django.urls import path
from cantores.views import listar_cantores, cadastrar_cantor, editar_cantor, excluir_cantor


urlpatterns = [
    path('',listar_cantores, name='listar_cantores'),
    path('cantores/cadastrar/', cadastrar_cantor,
    name='cadastrar_cantor'),
    path('cantores/editar/<int:id>/',editar_cantor,
    name= 'editar_cantor'),
    path('cantores/excluir/<int:id>/',excluir_cantor,
    name='excluir_cantor')
]