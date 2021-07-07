from django.shortcuts import render, redirect, HttpResponse
from pruebaApp1.models import Producto, Categoria
from .forms import CrearUsuarioForm
from django.contrib.auth import authenticate, login

# Create your views here.

def sobreNosotros(request):
    
    return render(request, "pruebas/sobreNosotros.html",)


def crearCuenta(request):
    return render(request, "pruebas/crearCuenta.html")    



def registro(request):
    
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            
            return redirect('indexProducto')  
    else:
        form = CrearUsuarioForm()
              
    return render(request, "registration/registro.html",{'form':form})





    
