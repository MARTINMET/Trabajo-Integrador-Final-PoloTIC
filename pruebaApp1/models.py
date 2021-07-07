from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f"Categoria: {self.nombre}" 

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='ProductosImg')
    descripcion = models.TextField()
    precio = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Producto#{self.id}: {self.nombre} / {self.categoria} / precio: ${self.precio} " 