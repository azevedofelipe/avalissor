from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Sum

# Tabela auxiliar de todos os cursos
class Curso(models.Model):
    curso = models.CharField(max_length=100)
    
    def __str__(self):
        return self.curso

# Tabela Auxiliar de faculdades
class Faculdade(models.Model):
    faculdade = models.CharField(max_length=100)

    def __str__(self):
        return self.faculdade

# Tabela principal de professores
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso,on_delete=models.PROTECT)
    faculdade = models.ForeignKey(Faculdade,related_name='faculdades',on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
    def nota_count(self):
        return self.avaliacao.count()
    
    def media_nota(self):
        avaliacao = Comentario.objects.filter(professor = self).aggregate(media=Avg('nota'))
        media = 0
        
        if avaliacao['media'] is not None:
            media = avaliacao['media']

        return media

    @property
    def faculdade_nome(self):
        return self.faculdade.faculdade
    
    @property
    def curso_nome(self):
        return self.curso.curso

# Tabela de comentarios e nota para cada professor
class Comentario(models.Model):
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,related_name='avaliacao')
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    texto = models.TextField()
    nota = models.IntegerField(default=5)   # nota de 1-5 estrelas
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["professor", "autor"], name="Apenas um comentario por professor")
        ]

    def __str__(self):
        return f'{self.autor.username} - {self.professor.nome} - {self.nota}'
    
    @property
    def professor_nome(self):
        return self.professor.nome
    

    @property
    def autor_nome(self):
        return self.autor.username
    
    @property
    def likes_sum(self):
        sum_likes = LikesComentarios.objects.filter(comentario = self).aggregate(sum_likes=Sum('like'))
        sum = 0
        
        if sum_likes['sum_likes'] is not None:
            sum = sum_likes['sum_likes']

        return sum
    
    @property
    def upvotes(self):
        upvotes = LikesComentarios.objects.filter(comentario=self,like=1).count()
        count = 0

        if upvotes:
            return upvotes
        
        return count


    @property
    def downvotes(self):
        downvotes = LikesComentarios.objects.filter(comentario=self,like=-1).count()
        count = 0

        if downvotes:
           return downvotes 

        return count

# Like para comentarios e avaliacoes de professores
class LikesComentarios(models.Model):
    like = models.IntegerField(default=0)   # +1 = Like, -1 = Dislike
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
     
    # Limit likes to one per author
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["comentario", "autor"], name="Apenas um like por comentario")
        ]


    def __str__(self):
        return f'{self.autor.username} - {self.like} - {self.comentario.autor.username}'
    
    @property
    def autor_nome(self):
        return self.autor.username
    
    @property
    def comentario_nome(self):
        return self.comentario.autor.username
    
    @property
    def professor_nome(self):
        return self.comentario.professor.nome