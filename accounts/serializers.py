from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    credits = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'credits')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Los créditos se asignan automáticamente a través del signal
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(instance, 'profile'):
            data['credits'] = instance.profile.credits
        else:
            data['credits'] = 2000  # valor por defecto
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Agregar información del usuario al token
        token['username'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        
        # Obtener o crear perfil de usuario para créditos
        try:
            if hasattr(user, 'profile'):
                credits = user.profile.credits
            else:
                # Crear perfil si no existe
                profile, created = UserProfile.objects.get_or_create(
                    user=user,
                    defaults={'credits': 2000}
                )
                credits = profile.credits
            
            token['credits'] = credits
        except Exception as e:
            # Valor por defecto en caso de error
            token['credits'] = 2000
        
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Agregar información adicional a la respuesta
        user = self.user
        
        # Obtener créditos actuales
        try:
            if hasattr(user, 'profile'):
                credits = user.profile.credits
            else:
                profile, created = UserProfile.objects.get_or_create(
                    user=user,
                    defaults={'credits': 2000}
                )
                credits = profile.credits
        except Exception:
            credits = 2000
        
        # Agregar datos a la respuesta
        data['user_info'] = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'credits': credits
        }
        
        return data