from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

# Create your views here.

def index(request):

    return render(request, 'Index.html',
    )

def crearComentario(request):
    comentario = Comentario.objects.all() 
    if request.method=='POST': 
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect('crearComentario')
    else:
        comentario_form= ComentarioForm()
    return render(request, 'core/form_crearcomentario.html', {'comentario_form': comentario_form,'datos': comentario})

def Ver(request):
    comentarios = Comentario.objects.all()

    return render(request, 'core/ver.html', context={'comentarios':comentarios})

def form_mod_comentario(request,id):
    comentario = Comentario.objects.get(correo=id)

    datos ={
        'form': ComentarioForm(instance=comentario)
    }
    if request.method == 'POST': 
        formulario = ComentarioForm(data=request.POST, instance = comentario)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'core/form_mod_comentario.html', datos)

def form_del_comentario(request,id):
    comentario = Comentario.objects.get(correo=id)
    comentario.delete()
    return redirect('ver')
