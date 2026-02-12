# Blog Técnico en Django

Este proyecto es un blog técnico sobre tecnología, desarrollado en Django siguiendo el patrón MVT.

## Requisitos
- Python 3.8+
- Django 4+
- Entorno virtual (recomendado)

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repo>
   ```
2. Activa el entorno virtual:
   ```bash
   # Windows
   venv\Scripts\activate
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

## Funcionalidades

### Modelos
- **Articulo**: título, contenido, fecha, categoría, autor, tags (grado de dificultad, opcional)
- **Categoria**: nombre, descripción
- **Autor**: nombre, email, bio

### Formularios
- Crear Artículo
- Crear Categoría
- Crear Autor
- Buscar Artículo por título o categoría

### Herencia de Plantillas
- `base.html`: plantilla base
- Otras plantillas heredan de `base.html`

## Orden para probar
1. Crear categorías y autores desde sus formularios.
2. Crear artículos, seleccionando categoría y autor.
3. Buscar artículos por título o categoría.

## Ubicación de funcionalidades
- Formularios: `/blog/articulo/nuevo/`, `/blog/categoria/nueva/`, `/blog/autor/nuevo/`
- Búsqueda: `/blog/buscar/`

## Contacto
Para dudas o sugerencias, contacta al autor del proyecto.

---

**Recuerda subir todo el proyecto a GitHub antes de entregar.**