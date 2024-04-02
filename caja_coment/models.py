from django.db import models

class Comentarios(models.Model):
  nombre = models.CharField(max_length=255)
  mensaje = models.CharField(max_length=255)
  
  def __str__(self):
    return f"{self.nombre} : {self.mensaje}"