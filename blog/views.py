
from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForm, CategoriaForm, AutorForm, BusquedaArticuloForm

# Vista para la página principal (listado de artículos)
def home(request):
	articulos = Articulo.objects.all().order_by('-fecha')
	return render(request, 'blog/home.html', {'articulos': articulos})

# Vista para crear un nuevo artículo
def crear_articulo(request):
	if request.method == 'POST':
		form = ArticuloForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ArticuloForm()
	return render(request, 'blog/articulo_form.html', {'form': form})

# Vista para crear una nueva categoría
def crear_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CategoriaForm()
	return render(request, 'blog/categoria_form.html', {'form': form})

# Vista para crear un nuevo autor
def crear_autor(request):
	if request.method == 'POST':
		form = AutorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = AutorForm()
	return render(request, 'blog/autor_form.html', {'form': form})

# Vista para buscar artículos por título o categoría
def buscar_articulo(request):
	resultados = []
	if request.method == 'GET':
		form = BusquedaArticuloForm(request.GET)
		if form.is_valid():
			consulta = form.cleaned_data.get('consulta')
			categoria = form.cleaned_data.get('categoria')
			articulos = Articulo.objects.all()
			if consulta:
				articulos = articulos.filter(titulo__icontains=consulta)
			if categoria:
				articulos = articulos.filter(categoria=categoria)
			resultados = articulos
	else:
		form = BusquedaArticuloForm()
	return render(request, 'blog/busqueda.html', {'form': form, 'resultados': resultados})
