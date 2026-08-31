from django.contrib import admin
from .models import Categoria, Receita

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...