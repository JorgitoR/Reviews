# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from Tienda.models import Producto

# Create your models here.

class departamento(models.Model):
    departamento= models.CharField(max_length=255)

    def __unicode__(self):
        return self.departamento


class Usuario(AbstractUser):
    femenino = models.BooleanField(default=False)
    masculino = models.BooleanField(default=False) 
    imagenperfil =  models.ImageField(upload_to='fotos_perfil', blank=True)
    biografia= models.TextField(max_length=100, default='')
    sitioweb=models.URLField(default='')
    educacion=models.CharField(max_length=100, default='')
    trabajo=models.CharField(max_length=100, default='')
    
    contacto = models.PositiveIntegerField(default=False, verbose_name="Numero de telefono")
    whatsap = models.PositiveIntegerField(default=False)
    departamento = models.ForeignKey(departamento, default=False )
    ciudad = models.CharField(max_length=100)

    calle = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100, verbose_name="Barrio")
    num_casa = models.CharField(max_length=100, verbose_name="Numero de casa")
    complemento = models.CharField(max_length=100, verbose_name="Complemento")

    


class info_compra(models.Model):

    producto = models.ForeignKey(Producto)