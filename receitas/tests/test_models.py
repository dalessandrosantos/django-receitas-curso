from django.test import TestCase
from receitas.models import Categoria, Receita
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User


class CategoriaModelTest(TestCase):
    """Testes do model Categoria."""

    def setUp(self):
        # Executado antes de cada teste para preparar os dados.
        self.categoria = Categoria.objects.create(nome='Chimarrão')

    def test_str_retorna_nome(self):
        # Testa o comportamento do método __str__().
        self.assertEqual(str(self.categoria), 'Chimarrão')

    def test_verbose_name(self):
        self.assertEqual(self.categoria._meta.verbose_name, 'Categoria')

    def test_verbose_name_plural(self):
        self.assertEqual(self.categoria._meta.verbose_name_plural, 'Categorias')


class ReceitaModelTest(TestCase):
    """Testes do model Receita."""

    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Chimarrão')

        # create_user() cria o usuário corretamente, incluindo o hash da senha.
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

            # Simula um upload de imagem durante o teste.
            capa=SimpleUploadedFile(
                name='capa_teste.jpg',
                content=b'conteudo_falso_da_imagem',
                content_type='image/jpeg'
            ),

            categoria=self.categoria,
            autor=self.autor,
        )

    def test_str_retorna_titulo(self):
        # Testa o comportamento do método __str__().
        self.assertEqual(str(self.receita), 'Chimarrão')

    def test_categoria_associada(self):
        # Testa o relacionamento entre Receita e Categoria.
        self.assertEqual(self.receita.categoria, self.categoria)

    def test_autor_associado(self):
        # Testa o relacionamento entre Receita e User.
        self.assertEqual(self.receita.autor, self.autor)

    def test_publicado_default_false(self):
        # Testa se o valor padrão do campo é False.
        self.assertFalse(self.receita.publicado)

    def test_tempo_preparo_unidade_default(self):
        self.assertEqual(self.receita.tempo_preparo_unidade, 'Minutos')

