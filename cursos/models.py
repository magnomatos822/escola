from os import name
from django.db import models


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.title


class Avaliacao(Base):
    curso = models.ForeignKey(
        "Curso", related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
