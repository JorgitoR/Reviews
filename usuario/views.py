# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, get_object_or_404, redirect

from .models import Usuario
from .forms import InformComprar
from Tienda.models import Producto


def comprar_producto(request, pk):

	tienda = get_object_or_404(Producto, pk=pk)

	if request.method == 'POST':
		form = InformComprar(request.POST or None, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('inicio')

	else:
		form=InformComprar(instance=request.user)

	context = {

		'tienda':tienda,
		'form':form
	}

	return render(request, 'informacion_comprar.html', context)


