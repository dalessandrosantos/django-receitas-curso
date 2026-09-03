from django.test import TestCase
from django.urls import reverse, resolve
from receitas import views

# reverse: nome da URL → caminho
# resolve: caminho → view

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