from rest_framework import serializers

from AuthApp.models import User, Producto


class UserSerializer(serializers.ModelSerializer):
    '''Serializador de usuarios'''
    class Meta:
        model = User
        fields = ['email', 'password', 'nombre', 'direccion', 'telefono', 'fecha_nacimiento']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'email': user.email,
            'nombre': user.nombre,
            'direccion': user.direccion,
            'telefono': user.telefono,
            'fecha_nacimiento': user.fecha_nacimiento
        }
    

class ProductoSerializer(serializers.ModelSerializer):
    '''Serializador de productos'''
    class Meta:
        model = Producto
        fields = ['nombre', 'valor', 'cantidad_inicial', 'owner']

    def to_representation(self, obj):
        producto = Producto.objects.get(id=obj.id)
        owner = User.objects.get(id=obj.owner)
        return {
            'id': producto.id,
            'nombre': producto.nombre,
            'valor': producto.valor,
            'cantidad_inicial': producto.cantidad_inicial,
            'owner': {
                'id': owner.id,
                'email': owner.email
            }
        }