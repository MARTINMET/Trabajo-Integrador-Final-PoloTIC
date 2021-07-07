from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto, Categoria
from .forms import CargarProductoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
# Create your views here.


def indexProducto(request):
  
    productos= Producto.objects.all().order_by('-id')
    return render(request,"pruebaApp1/indexProducto.html",{"productos": productos})


def Vistaproducto(request, producto_id):
    
    
    productos=Producto.objects.get(id=producto_id)

    return render(request,"pruebaApp1/Vistaproducto.html", {"productos": productos})


def ListaCategorias(request, categoria_id):
    
    categoria=Categoria.objects.get(id=categoria_id)
    productos= Producto.objects.filter(categoria=categoria)
    return render(request,"pruebaApp1/ListaCategorias.html", {"categoria": categoria,"productos": productos})         



def listaBusqueda(request):
    
        buscar= request.GET.get('buscar')
        productos=Producto.objects.all()
         
        if buscar:
         productos=Producto.objects.filter(
            Q(descripcion__icontains=buscar) |
            Q(nombre__icontains=buscar)
            )
        return render(request,"pruebaApp1/listaBusqueda.html", {"productos": productos})


@permission_required('pruebaApp1.add_producto')
def cargarProducto(request):

    if request.method == 'POST':
        form = CargarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('indexProducto')  
    else:
        form = CargarProductoForm()
              
    return render(request, "pruebaApp1/cargarProducto.html",{'form':form})



@permission_required('pruebaApp1.change_producto')
def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":  
        form = CargarProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('indexProducto')
    else:
        form = CargarProductoForm(instance = producto)
    
    
    return render(request,"pruebaApp1/editarProducto.html",{'form':form,'producto':producto})

@permission_required('pruebaApp1.delete_producto')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect('indexProducto')




    

        
    

    


    