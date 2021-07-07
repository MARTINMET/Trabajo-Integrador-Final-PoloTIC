from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexProducto, name="indexProducto"),
    path('Vistaproducto/<int:producto_id>/',views.Vistaproducto, name="Vistaproducto"),
    path('ListaCategorias/<int:categoria_id>/',views.ListaCategorias, name="ListaCategorias"),
    path('listaBusqueda/',views.listaBusqueda, name="listaBusqueda"),
    path('cargarProducto/',views.cargarProducto, name="cargarProducto"),
    path('editarProducto/<int:id>/',views.editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>/',views.eliminarProducto, name="eliminarProducto"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)