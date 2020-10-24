# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from resena.models import Review
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Producto(models.Model):
    titulo = models.CharField(max_length=40, unique=True)
    img = models.FileField(upload_to='photos/')
    descripcion = models.TextField(verbose_name="Descripción")

    reviews = GenericRelation(Review, related_query_name="product")

    def __unicode__(self):
        return self.titulo


    @property 
    def reviews(self):
        instance =self
        qs = Review.objects.filtrar_por_instancia(instance)
        return qs
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(Producto)
        return content_type 
    