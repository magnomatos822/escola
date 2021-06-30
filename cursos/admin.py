from django.contrib import admin
from .models import Avaliacao, Curso


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'create', 'update', 'active')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create', 'update', 'active')


