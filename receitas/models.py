from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Receita(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    slug = models.SlugField()
    tempo_preparo = models.IntegerField()
    tempo_preparo_unidade = models.CharField(max_length=20, default='Minutos')
    modo_preparo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='receitas/capas/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo