from django import forms
from .models import Development

class ImagesForm(forms.Form):
    development = forms.ModelChoiceField(queryset=Development.objects.all(), label='development', widget=forms.Select(attrs={'class': "form-control"}))