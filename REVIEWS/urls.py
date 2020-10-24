"""REVIEWS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from Tienda.views import(

	inicio,
	producto_ver,

	)

from usuario.views import(

        comprar_producto

    )


urlpatterns = [


    url(r'^admin/', admin.site.urls),

    url(r'^$', inicio, name='inicio'),    

    url(r'^producto_ver(?P<pk>\d+)/$', producto_ver, name='producto_ver'),
    
    url(r'^comprar/(?P<pk>\d+)/$', comprar_producto, name='comprar'),


]



if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)