from .models import Comentario, Professor
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

    class Meta:
        model = Comentario
        fields = ('id','professor','professor_nome','nota','autor','autor_nome','texto')