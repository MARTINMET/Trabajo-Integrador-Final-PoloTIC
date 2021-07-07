from django.contrib import admin
from.models import Producto, Categoria


# Register your models here.

class ProductoCreado(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria)
admin.site.register(Producto, ProductoCreado)