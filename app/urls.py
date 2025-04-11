from . import views
from django.urls import path

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateView.as_view(), name='listar_aniversariante'),
]