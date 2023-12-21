from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from .forms import *


def ver_clases(request):
    clases = Clase.objects.all().order_by('id')
    return render(request, 'Clases/ver_clases.html', { 'clases' : clases })


def buscar_clases(request):
    nombre = request.GET.get('nombre', None)

    if nombre:
        clases = Clase.objects.filter(nombre__icontains=nombre)
    else:
        clases = Clase.objects.all()

    clases = clases.order_by('id')

    formulario_buscar_clases = FormularioBuscarClase()

    return render(request, 'Clases/buscar_clases.html', { 'formulario_buscar_clases' : formulario_buscar_clases, 'clases' : clases })


class VerClaseView(DetailView):
    model = Clase
    template_name = 'Clases/ver_clase.html'


class NuevaClaseView(LoginRequiredMixin, CreateView):
    model = Clase
    template_name = 'Clases/crear_clase.html'
    success_url = '/clases/'
    fields = ['nombre', 'descripcion', 'codigo', 'imagen', 'rutina']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarClaseView(LoginRequiredMixin, UpdateView):
    model = Clase
    template_name = 'Clases/editar_clase.html'
    success_url = '/clases/'
    fields = ['nombre', 'descripcion', 'codigo', 'imagen', 'rutina']


class EliminarClaseView(LoginRequiredMixin, DeleteView):
    model = Clase
    template_name = 'Clases/borrar_clase.html'
    success_url = '/clases/'