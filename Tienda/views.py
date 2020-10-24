# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Producto
from resena.forms import formReviews
from resena.models import Review

from django.db.models import Count

from django.contrib.contenttypes.models import ContentType
# Create your views here.

def inicio(request):

	tienda = Producto.objects.all()

	context = {

		'tienda':tienda,
	}

	return  render(request, 'inicio.html', context)


def producto_ver(request, pk):

        instance = get_object_or_404(Producto, pk=pk)

        initial_data = {
            "content_type": instance.get_content_type,
            "object_id":instance.id,

        }


        form = formReviews(request.POST or None, initial=initial_data)
        if form.is_valid():
            contenido = form.cleaned_data.get("content_type")
            content_type =ContentType.objects.get(model=contenido)
            obj_id = form.cleaned_data.get("object_id")
            content_data = form.cleaned_data.get("contenido")
            score_data = form.cleaned_data.get("puntaje")
    
            new_reviews, created = Review.objects.get_or_create(
                                user = request.user,
                                content_type = content_type,
                                object_id= obj_id,
                                comment = content_data,
                                score = score_data


                                    )

            return HttpResponseRedirect(new_reviews.content_object.get_absolute_url())

            if created:
                print("yeah it worked")

        d = instance.reviews

        reviews = instance.reviews
        total_1 = instance.reviews.filter(score__in="1").count()
        total_2 = instance.reviews.filter(score__in="2").count()
        total_3 = instance.reviews.filter(score__in="3").count()
        total_4 = instance.reviews.filter(score__in="4").count()
        total_5 = instance.reviews.filter(score__in="5").count()
        score_1 = instance.reviews.filter(score__in="1")
        score_2 = instance.reviews.filter(score__in="2")
        score_3 = instance.reviews.filter(score__in="3")
        score_4 = instance.reviews.filter(score__in="4")
        score_5 = instance.reviews.filter(score__in="5")

        context = {
            'tienda': instance,
            'reviews':reviews, 
            'score_1':score_1,
            'score_2':score_2,
            'score_3':score_3,
            'score_4':score_4,
            'score_5':score_5,
            'total_1':total_1,
            'total_2':total_2,
            'total_3':total_3,
            'total_4':total_4,
            'total_5':total_5,
            "form":form,

         }

        return render(request, 'ver_producto.html', context)
