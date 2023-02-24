from django.db import models

from .user import User


class Producto(models.Model):
    '''Modelo de productos'''
    id = models.SmallAutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='producto_u', on_delete=models.CASCADE)
    nombre = models.CharField('Productos', max_length=50)
    valor = models.IntegerField('Valor')
    cantidad_inicial = models.IntegerField('Cantidad inicial')

    