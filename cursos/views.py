from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursosSerializer


class AvaliacaoAPIView(APIView):
    """
    Api de Cursos

    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class CursosAPIView(APIView):
    """
    Api de Cursos
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursosSerializer(cursos, many=True)
        return Response(serializer.data)
