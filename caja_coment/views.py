from django.shortcuts import render
from .forms import CreateComentario
from .models import Comentarios
def caja_coment(request):
    
    form = CreateComentario
    
    if request.method == "POST":
           # print(request.POST['nombre'])
           form = CreateComentario(request.POST)
           
           if form.is_valid():
                   print("valido")
                  
                   comentarios= Comentarios()
                   
                   comentarios.nombre = form.cleaned_data['nombre']
                   comentarios.mensaje = form.cleaned_data['mensaje']
                  
                   comentarios.save()
           else:
                   print("invalido")        
            
    return render(request, 'coment.html' ,{'form' : form}) 