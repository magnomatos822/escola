from django.urls import path

from .views import AvaliacaoAPIView, CursosAPIView

urlpatterns = [
    path('avaliacao/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
    path('curso', CursosAPIView.as_view(), name='cursos')
]
