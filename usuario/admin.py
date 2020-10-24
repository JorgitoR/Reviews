# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
 
from .models import departamento 
from .models import Usuario

admin.site.register(departamento)
admin.site.register(Usuario)