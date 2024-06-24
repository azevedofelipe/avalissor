from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Professor,Comentario,LikesComentarios
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
   
def professor_list(request):
    professores = Professor.objects.all()
    return render(request,'professors.html',{'professores':professores})


def professor_details(request,prof_id):
    professor = Professor.objects.get(id=prof_id)
    comments = Comentario.objects.filter(professor_id=prof_id).all()
    return render(request, 'professor_details.html', {'professor': professor, 'comments': comments}) 

@login_required(login_url='/auth/login/')          
def create_comment(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    
    if request.method == 'POST':
        texto = request.POST['texto']
        nota = request.POST.get('nota', 5)  # Default to 5 if no rating is selected
        
        comentario = Comentario.objects.filter(professor=professor,autor=request.user).first()

        if comentario:
            return HttpResponse("Ja existe")
        
        # Create the comment
        comentario = Comentario(
            professor=professor,
            autor=request.user,
            texto=texto,
            nota=nota
        )
        comentario.save()
        
        # Redirect to the professor detail page or wherever you want after submission
        return redirect('professor:professor_details',prof_id=professor.pk)


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