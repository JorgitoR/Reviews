
from django import forms
from .models import info_compra
from django.contrib.auth.models import User

from .models import Usuario

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class InformComprar(forms.ModelForm):
    

    class Meta:
        model = Usuario
        fields = (
        
            'first_name',
            'last_name',
	     	'departamento',
	     	'ciudad',
	     	'calle',
	     	'barrio',
	     	'num_casa',
	     	'complemento'

        )