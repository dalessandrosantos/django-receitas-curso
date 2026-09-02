from django.test import TestCase
from receitas.models import Categoria, Receita
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User


class CategoriaModelTest(TestCase):
    """Testes do model Categoria: string de exibição e metadados (Meta)."""

    def setUp(self):
        # Objeto base reutilizado em todos os testes desta classe
        self.categoria = Categoria.objects.create(nome='Chimarrão')


    #   Métodos de Testes
    def test_str_retorna_nome(self):
        # __str__ deve expor o nome da categoria (usado no admin, templates, etc.)
        self.assertEqual(str(self.categoria), 'Chimarrão')

    def test_verbose_name(self):
        # Nome amigável (singular) definido na Meta class
        self.assertEqual(self.categoria._meta.verbose_name, 'Categoria')

    def test_verbose_name_plural(self):
        # Nome amigável (plural) — evita o Django "adivinhar" errado em português
        self.assertEqual(self.categoria._meta.verbose_name_plural, 'Categorias')


class ReceitaModelTest(TestCase):
    """Testes do model Receita, incluindo relações (FK) com Categoria e User."""

    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Chimarrão')

        # create_user() garante o hash correto da senha (nunca usar .create() aqui)
        self.autor = User.objects.create_user(
            username='dalessandro',
            password='senha123'
        )

        self.receita = Receita.objects.create(
            titulo='Chimarrão',
            descricao='Uma receita clássica de chimarrão gaúcho.',
            slug='chimarrao-tradicional',
            tempo_preparo=10,
            modo_preparo='Aqueça a água, monte a cuia e sirva.',

            # ImageField é obrigatório no model — simula um upload sem precisar de arquivo real
            capa=SimpleUploadedFile(
                name='capa_teste.jpg',
                content=b'conteudo_falso_da_imagem',
                content_type='image/jpeg'
            ),


            categoria=self.categoria,
            autor=self.autor,
        )


    #   Métodos de testes
    def test_str_retorna_titulo(self):
        # __str__ deve expor o título da receita
        self.assertEqual(str(self.receita), 'Chimarrão')

    def test_categoria_associada(self):
        self.assertEqual(self.receita.categoria, self.categoria)

    def test_autor_associado(self):
        self.assertEqual(self.receita.autor, self.autor)

    def test_publicado_default_false(self):
        self.assertFalse(self.receita.publicado)

    def test_tempo_preparo_unidade_default(self):
        self.assertEqual(self.receita.tempo_preparo_unidade, 'Minutos')