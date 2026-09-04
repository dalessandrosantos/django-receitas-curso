from django.test import TestCase                              # Classe base para testes Django
from django.urls import reverse                                # Converte nome de URL em path
from django.contrib.auth.models import User                    # Model de usuário, usado como autor
from django.core.files.uploadedfile import SimpleUploadedFile  # Simula upload de arquivo (campo capa)
from receitas.models import Categoria, Receita                 # Models testados


class HomeViewTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Chimarrão')

        self.autor = User.objects.create_user(
            username='dalessandro',
            password='senha123'
        )

        # Receita publicada — deve aparecer na home
        self.receita_publicada = Receita.objects.create(
            titulo='Chimarrão Tradicional',
            descricao='Uma receita clássica de chimarrão gaúcho.',
            slug='chimarrao-tradicional',
            tempo_preparo=10,
            modo_preparo='Aqueça a água, monte a cuia e sirva.',
            capa=SimpleUploadedFile(
                name='capa_publicada.jpg',
                content=b'conteudo_falso',
                content_type='image/jpeg'
            ),
            categoria=self.categoria,
            autor=self.autor,
            publicado=True,
        )

        # Receita NÃO publicada — não deve aparecer na home
        self.receita_nao_publicada = Receita.objects.create(
            titulo='Chimarrão Rascunho',
            descricao='Ainda em teste, não deveria aparecer.',
            slug='chimarrao-rascunho',
            tempo_preparo=5,
            modo_preparo='Rascunho de receita.',
            capa=SimpleUploadedFile(
                name='capa_rascunho.jpg',
                content=b'conteudo_falso',
                content_type='image/jpeg'
            ),
            categoria=self.categoria,
            autor=self.autor,
            publicado=False,
        )

    def test_home_status_code(self):
        """Testa se a página inicial carrega com sucesso (status 200)."""
        url = reverse('receitas-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_usa_template_correto(self):
        """Testa se a view home renderiza o template correto."""
        url = reverse('receitas-home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'receitas/paginas/home.html')

    def test_home_contexto_tem_receita_publicada(self):
        """Testa se uma receita publicada aparece no contexto da home."""
        url = reverse('receitas-home')
        response = self.client.get(url)
        self.assertIn(self.receita_publicada, response.context['receitas'])

    def test_home_contexto_nao_tem_receita_nao_publicada(self):
        """Testa se uma receita não publicada NÃO aparece no contexto da home."""
        url = reverse('receitas-home')
        response = self.client.get(url)
        self.assertNotIn(self.receita_nao_publicada, response.context['receitas'])


class CategoriaViewTest(TestCase):
    def setUp(self):
        self.categoria_com_receita = Categoria.objects.create(nome='Chimarrão')
        self.categoria_sem_receita = Categoria.objects.create(nome='Tereré')

        self.autor = User.objects.create_user(
            username='dalessandro',
            password='senha123'
        )

        self.receita_publicada = Receita.objects.create(
            titulo='Chimarrão Tradicional',
            descricao='Uma receita clássica de chimarrão gaúcho.',
            slug='chimarrao-tradicional',
            tempo_preparo=10,
            modo_preparo='Aqueça a água, monte a cuia e sirva.',
            capa=SimpleUploadedFile(
                name='capa.jpg',
                content=b'conteudo_falso',
                content_type='image/jpeg'
            ),
            categoria=self.categoria_com_receita,
            autor=self.autor,
            publicado=True,
        )

    def test_categoria_status_code(self):
        """Testa se a página de uma categoria com receita publicada carrega com sucesso."""
        url = reverse('categoria', kwargs={'categoria_id': self.categoria_com_receita.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categoria_usa_template_correto(self):
        """Testa se a view categoria renderiza o template correto"""
        url = reverse('categoria', kwargs={'categoria_id': self.categoria_com_receita.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'receitas/paginas/categoria.html')

    def test_categoria_contexto_tem_receita_publicada(self):
        """Testa se a receita publicada da categoria aparece no contexto."""
        url = reverse('categoria', kwargs={'categoria_id': self.categoria_com_receita.id})
        response = self.client.get(url)
        self.assertIn(self.receita_publicada, response.context['receitas'])

    def test_categoria_sem_receita_publicada_retorna_404(self):
        """Testa se uma categoria sem receita publicada retorna 404."""
        url = reverse('categoria', kwargs={'categoria_id': self.categoria_sem_receita.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ReceitaViewTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Chimarrão')

        self.autor = User.objects.create_user(
            username='dalessandro',
            password='senha123'
        )

        self.receita_publicada = Receita.objects.create(
            titulo='Chimarrão Tradicional',
            descricao='Uma receita clássica de chimarrão gaúcho.',
            slug='chimarrao-tradicional',
            tempo_preparo=10,
            modo_preparo='Aqueça a água, monte a cuia e sirva.',
            capa=SimpleUploadedFile(
                name='capa.jpg',
                content=b'conteudo_falso',
                content_type='image/jpeg'
            ),
            categoria=self.categoria,
            autor=self.autor,
            publicado=True,
        )

        self.receita_nao_publicada = Receita.objects.create(
            titulo='Chimarrão Rascunho',
            descricao='Ainda em teste.',
            slug='chimarrao-rascunho',
            tempo_preparo=5,
            modo_preparo='Rascunho.',
            capa=SimpleUploadedFile(
                name='capa2.jpg',
                content=b'conteudo_falso',
                content_type='image/jpeg'
            ),
            categoria=self.categoria,
            autor=self.autor,
            publicado=False,
        )


    def test_receita_status_code(self):
        """Testa se a página de uma receita publicada carrega com sucesso (status 200)."""
        url = reverse('receitas-receita', kwargs={'id': self.receita_publicada.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_receita_usa_template_correto(self):
        """Testa se a view receita renderiza o template correto."""
        url = reverse('receitas-receita', kwargs={'id': self.receita_publicada.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'receitas/paginas/receita-view.html')

    def test_receita_context_tem_receita(self):
        """Testa se a receita publicada correta aparece no contexto."""
        url = reverse('receitas-receita', kwargs={'id': self.receita_publicada.id})
        response = self.client.get(url)
        self.assertEqual(response.context['receita'], self.receita_publicada)

    def test_receita_nao_publicada_retorna_404(self):
        """Testa se uma receita não publicada retorna 404."""
        url = reverse('receitas-receita', kwargs={'id': self.receita_nao_publicada.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)