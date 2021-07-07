from django.urls import path
from pruebas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sobreNosotros/',views.sobreNosotros, name="SobreNosotros"),
    path('registro/',views.registro, name="registro"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)