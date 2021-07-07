from pruebaApp1.models import Producto
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    listaProductos=models.ManyToManyField(Producto)


    def __str__(self):
        return f"{self.usuario} - {self.listaProductos}"
