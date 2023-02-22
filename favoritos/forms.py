from django import forms
from .models import Favoritos

class FavoritoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    url = forms.CharField(label='Url', max_length=100)

class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = ['nombre', 'url'] # '__all__' means