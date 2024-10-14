from django import forms
from .models import Noticia ,Categoria

class NotiForm(forms.ModelForm):
    class Meta: # faltaba esta linea
        model = Noticia
        fields = ['titulo',	'bajada', 'cuerpo', 'imagen', 'categoria_noticia','usuario']

class CategForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields =['nombre']

