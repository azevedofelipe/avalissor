from django.shortcuts import render
from avalissor.permissions import isOwner
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Professor,Comentario,LikesComentarios
from .serializers import ProfessorSerializer,ComentarioSerializer, LikesComentarioSerializer
from django_filters import rest_framework as filters 

# API para listar todos os professores
#class ProfessorList(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticatedOrReadOnly,]
#
#    filter_backends = (filters.DjangoFilterBackend,)
#    filterset_fields = {
#        'nome' : ['contains'],
#        'faculdade' : ['in'],
#        'curso' : ['in']
#    }
#    serializer_class = ProfessorSerializer
#    queryset = Professor.objects.all().distinct()
    
def professor_list(request):
    professores = Professor.objects.all()
    return render(request,'professors.html',{'professores':professores})


# API para RUD de professores C[RUD]
#class ProfessorDetalhes(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = [isOwner,]
#
#    serializer_class = ProfessorSerializer
#    queryset = Professor.objects.all()
#
#
## API para criar comentario
#class ComentarioCriar(generics.ListCreateAPIView):
#    permission_classes = (IsAuthenticatedOrReadOnly,)
#
#    serializer_class = ComentarioSerializer
#    queryset = Comentario.objects.all()
#
#
## API para ver detalhes de comentario
#class ComentarioDetalhes(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = (isOwner,)
#
#    serializer_class = ComentarioSerializer
#    queryset = Comentario.objects.all()
#    
#
## API para likes para comentarios
#class LikeCriar(generics.ListCreateAPIView):
#    permission_classes = (IsAuthenticatedOrReadOnly,)
#    
#    serializer_class = LikesComentarioSerializer
#    queryset = LikesComentarios.objects.all()
#
#
## API para alterar like
#class LikeDetalhes(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = (isOwner,)
#
#    serializer_class = LikesComentarioSerializer
#    queryset = LikesComentarios.objects.all()