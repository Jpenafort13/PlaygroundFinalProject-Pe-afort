from django.urls import path
from .views import *

urlpatterns = [
    path('', ver_clases, name='ver_clases'),
    path('buscar/', buscar_clases, name='buscar_clases'),
    path('clase/<int:pk>', VerClaseView.as_view(), name='ver_clase'),
    path('nuevo/', NuevaClaseView.as_view(), name='crear_clase'),
    path('clase/<int:pk>/editar/', EditarClaseView.as_view(), name='editar_clase'),
    path('clase/<int:pk>/eliminar/', EliminarClaseView.as_view(), name='borrar_clase'),
]