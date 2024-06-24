from .models import Comentario, Professor, LikesComentarios
from rest_framework import serializers

# Serializer para modelo Lugar
class ProfessorSerializer(serializers.ModelSerializer):
    faculdade_nome = serializers.ReadOnlyField()
    curso_nome = serializers.ReadOnlyField()

    class Meta:
        model = Professor 
        fields = ('id','nome','curso','curso_nome','faculdade','faculdade_nome','nota_count','media_nota')


class ComentarioSerializer(serializers.ModelSerializer):
    professor_nome = serializers.ReadOnlyField()
    autor_nome = serializers.ReadOnlyField()
    likes_sum = serializers.ReadOnlyField()
    upvotes = serializers.ReadOnlyField()
    downvotes = serializers.ReadOnlyField()

    class Meta:
        model = Comentario
        fields = ('id','professor','professor_nome','nota','autor','autor_nome','texto','upvotes','downvotes','likes_sum')
        

class LikesComentarioSerializer(serializers.ModelSerializer):
    autor_nome = serializers.ReadOnlyField()
    comentario_nome = serializers.ReadOnlyField()
    professor_nome = serializers.ReadOnlyField()

    class Meta:
        model = LikesComentarios
        fields = ('id','like','autor_nome','comentario_nome','professor_nome')