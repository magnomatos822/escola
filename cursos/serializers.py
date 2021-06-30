from rest_framework import serializers
from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'create',
            'update',
            'active'
        )


class CursosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'title',
            'url',
            'create',
            'update',
            'active'
        )
