from django.contrib import admin
from .models import Comentario,Professor,Curso,Faculdade,LikesComentarios

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Faculdade)
admin.site.register(LikesComentarios)