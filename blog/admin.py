
from django.contrib import admin
from .models import Categoria, Autor, Articulo

# Registrar el modelo Categoria en el panel de administración
admin.site.register(Categoria)

# Registrar el modelo Autor en el panel de administración
admin.site.register(Autor)

# Registrar el modelo Articulo en el panel de administración
admin.site.register(Articulo)
