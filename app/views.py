from django.shortcuts import render
from .models import Aniversariante
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AniversarianteSerializer, ObterTokenSerializer, serializers
from rest_framework.pagination import PageNumberPagination
import re
from rest_framework_simplejwt.views import TokenObtainPairView

class AiversariantePaginacao(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class AniversarianteListCreateView(ListCreateAPIView):
    queryset = Aniversariante.objects.all()
    serializer_class = AniversarianteSerializer
    pagination_class = AiversariantePaginacao

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        cpf = serializer.validated_data['CPF']
        data = serializer.validated_data['data']
        idade = serializer.validated_data['idade']

        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            error_cpf = True
        
        if data.year + idade != 2025:
            error_data = True
        
        if error_cpf:
            raise serializers.ValidationError('CPF inválido. O CPF deve estar no formato XXX.XXX.XXX-XX')
        elif error_data:
            raise serializers.ValidationError('A sua idade não corresponde à data que você selecionou.')
        else:
            raise serializers.ValidationError('CPF inválido e a sua idade não corresponde à data que você selecionou.')
        serializer.save()

class AniversarianteRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Aniversariante.objects.all()
    serializer_class = AniversarianteSerializer
    lookup_field = 'pk'

class LoginView(TokenObtainPairView):
    serializer_class = ObterTokenSerializer
    