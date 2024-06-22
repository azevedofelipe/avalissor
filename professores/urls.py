from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [
    path('',views.ProfessorList.as_view()),                     # Lista de professores
    path('<int:pk>/',views.ProfessorDetalhes.as_view()),        # Detalhes de professor, pk de professor especifico
    path('comentarios',views.ComentarioCriar.as_view()),
    path('comentarios/<int:pk>',views.ComentarioDetalhes.as_view())
]