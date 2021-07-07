from django.shortcuts import redirect, render, get_object_or_404
from pruebaApp1.models import Producto, Categoria
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.




def carrito(request):
     
    return render(request,"carrito/carrito.html")




