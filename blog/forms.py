from django import forms
from .models import Articulo, Categoria, Autor

# Formulario para crear un nuevo artículo
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'autor', 'tags']
        widgets = {
            'tags': forms.Select(attrs={'class': 'form-select'}),
        }

# Formulario para crear una nueva categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

# Formulario para crear un nuevo autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'bio']

# Formulario para buscar artículos por título o categoría
class BusquedaArticuloForm(forms.Form):
    consulta = forms.CharField(label='Buscar por título', max_length=100, required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
