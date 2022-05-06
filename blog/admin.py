from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Con Import y export agregamos botones en el panel de administración, esto se instala, hay que buscar la documentacion para saber como instalarlo.

class CategoriaResource(resources.ModelResource):
    class Meta:
        models = Categoria
    

# Con este codigo lo que hago es modificar el admin de la pagina.

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre'] # Creamos un buscador
    list_display = ('nombre', 'estado', 'fecha_creacion', ) # Creamos los nombres del cada categoria, o sea el ecabezado
    resources_class = CategoriaResource
    
class AutorResource(resources.ModelResource):
    class Meta:
        models = Autor
    
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos','correo'] 
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion')
    resources_class = AutorResource
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)

# Register your models here.
