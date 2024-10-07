from django.db import models
from estilos.models import Estilo

class Cantores(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    estilos = models.ForeignKey(Estilo,on_delete=models.CASCADE,default='SP')

    def __str__(self):
        return self.nome
