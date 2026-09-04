from django.test import TestCase           # Classe base para testes Django
from django.urls import reverse, resolve   # reverse: nome → path | resolve: path → view
from receitas import views                 # Módulo de views, usado para comparar a função resolvida

class receitasHomeUrlsTest(TestCase):
    def test_home_url_resolve(self):
        """Testa se a URL da página inicial aponta para a view correta."""
        url = reverse('receitas-home')
        self.assertEqual(resolve(url).func, views.home)

    def test_categoria_url_resolve(self):
        """Testa se a URL de uma categoria aponta para a view correta."""
        url = reverse('categoria', kwargs={'categoria_id': 1})
        self.assertEqual(resolve(url).func, views.categoria)

    def test_receita_url_resolve(self):
        """Testa se a URL de uma receita aponta para a view correta."""
        url = reverse('receitas-receita', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, views.receita)