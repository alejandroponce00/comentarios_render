from django.urls import path

from . import views

urlpatterns = [
    path('', views.caja_coment, name='caja_coment'),
]