from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Tabela auxiliar de todos os cursos
class Cursos(models.Model):
    curso = models.CharField(max_length=100)

# Tabela Auxiliar de faculdades
class Faculdades(models.Model):
    faculdade = models.CharField(max_length=100)

# Tabela principal de professores
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Cursos,on_delete=models.PROTECT)
    faculdade = models.ForeignKey(Faculdades,related_name='faculdades',on_delete=models.PROTECT)

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
    
    def __str__(self):
        return f'{self.autor.username} - {self.professor.nome}'
    
    @property
    def professor_nome(self):
        return self.professor.nome
    

    @property
    def autor_nome(self):
        return self.autor.username