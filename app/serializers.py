from rest_framework import serializers
from .models import Aniversariante, Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AniversarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aniversariante
        fields = '__all__'
        read_only_fields = ['id'] 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data ['usuario'] = {
            'username': self.user.username,
            'email': self.user.email,
            'foto_perfil': self.user.foto_perfil.url
        }

        return data
    
class ObterTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            usuario = authenticate(request=self.context.get('request'), username=username, password=password)

            if not usuario:
                raise serializers.ValidationError('Usuário ou senha inválidos.', code='authorization')
        
        else:
            raise serializers.ValidationError('Usuário e senha são obrigatórios.', code='authorization')

        attrs['usuario'] = UsuarioSerializer(usuario).data
        return attrs
