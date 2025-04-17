from . import views
from django.urls import path

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateView.as_view(), name='listar_aniversariante'),
    path('aniversariante/<int:pk>/', view=views.AniversarianteRetriveUpdateDestroyView.as_view(), name='atualizar_deletar_visualizar_aniversariante')
]