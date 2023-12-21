from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Clase(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    codigo = models.IntegerField()
    rutina = RichTextField(null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    imagen = models.ImageField(upload_to='galeria')
