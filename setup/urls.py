
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estilo/',include('estilos.urls')),
   path('',include('cantores.urls')),
]



