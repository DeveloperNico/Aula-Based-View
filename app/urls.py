from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateView.as_view(), name='listar_aniversariante'),
    path('aniversariante/<int:pk>/', view=views.AniversarianteRetriveUpdateDestroyView.as_view(), name='atualizar_deletar_visualizar_aniversariante')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)