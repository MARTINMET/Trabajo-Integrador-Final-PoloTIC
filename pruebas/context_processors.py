from pruebaApp1.models import Categoria



def menu_categorias(request):
    categorias= Categoria.objects.all().order_by('-id')
    return {"categorias": categorias}


 