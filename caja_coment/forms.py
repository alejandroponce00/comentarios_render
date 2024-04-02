from django import forms
class CreateComentario(forms.Form):
     nombre=forms.CharField(label="Nombre", max_length=200)
     mensaje=forms.CharField(label = "Ingrese su comentario" ,widget=forms.Textarea)   