from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Noticia, Comentario

class ComentarioForm(forms.ModelForm):

    class Meta: 
        model= Comentario
        fields = ['correo', 'nombre', 'comentario', 'noticia']
        labels ={
            'correo': 'Correo', 
            'nombre': 'Nombre', 
            'comentario': 'Comentario', 
            'noticia': 'Noticia',
        }
        widgets={
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su comentario', 
                    'id': 'comentario'
                }
            ), 
            'pelicula': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'noticia',
                }
            )

        }