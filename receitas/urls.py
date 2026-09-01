from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="receitas-home"),
    path('receitas/categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('receitas/<int:id>/', views.receita, name='receitas-receita'),
]
