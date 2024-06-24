from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [
    path('',views.ProfessorList.as_view()),                     # Lista de professores
    path('<int:pk>/',views.ProfessorDetalhes.as_view()),        # Detalhes de professor, pk de professor especifico
    path('comentarios',views.ComentarioCriar.as_view()),        # Criar Comentarios sobre professor
    path('comentarios/<int:pk>',views.ComentarioDetalhes.as_view()), # Detalhes de comentario, editar se for dono
    path('likes',views.LikeCriar.as_view()),    # Criar Likes para comentarios
    path('likes/<int:pk>',views.LikeDetalhes.as_view()) # Alterar like

]