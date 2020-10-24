from django import forms

class formReviews(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	contenido = forms.CharField(label='', widget=forms.Textarea)
	puntaje = forms.IntegerField()