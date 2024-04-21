from django.shortcuts import render
from .forms import CreateComentario
from .models import Comentarios

def caja_coment(request):
    form = CreateComentario()

    if request.method == "POST":
        form = CreateComentario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            Comentarios.objects.create(nombre=nombre, mensaje=mensaje)  # Crear un nuevo comentario en la base de datos

    # Obtener todos los comentarios
    comentarios = Comentarios.objects.all()

    return render(request, 'coment.html', {'form': form, 'comentarios': comentarios})
