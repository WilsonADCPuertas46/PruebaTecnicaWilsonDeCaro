from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    '''Administrador de usuarios'''

    def create_user(self, email, password=None):
        '''Creacion de usuarios'''
        if not email:
            raise ValueError('Coloque su email')
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        '''Creacion de superusuarios'''

        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Modelo de usuarios'''
    id = models.SmallAutoField(primary_key=True)
    email = models.EmailField('Correo', unique=True)
    password = models.CharField('Contraseña', max_length=100)
    nombre = models.CharField('Nombre', max_length=50)
    direccion = models.CharField('Dirección', max_length=40)
    telefono = models.IntegerField('Télefono')
    fecha_nacimiento = models.DateField('Fecha de nacimiento')


    def save(self, *args, **kwargs):
        some_salt = 'Qu32oNH0l4nDe2'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)


    objects = UserManager()        
    USERNAME_FIELD = 'email'