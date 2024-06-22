from django.contrib import admin
from .models import Comentario,Professor,Curso,Faculdade

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Faculdade)
