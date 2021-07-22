from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Noticia(models.Model):

    idNoticia = models.IntegerField(primary_key=True, verbose_name='Id de Noticia')

    nombreNoticia = models.CharField(max_length=50, verbose_name='Nombre de la Noticia')



    def str(self):

        return (self.nombreNoticia)


class Comentario(models.Model):

    correo = models.CharField(max_length=100, primary_key=True, verbose_name='Correo')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    comentario = models.CharField(max_length=150, verbose_name='Comentario')
    pnoticia = models.ForeignKey(Noticia, on_delete=CASCADE)



    def str(self):

        return (self.correo)