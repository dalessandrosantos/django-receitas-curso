from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('receitas/<int:id>/', views.receita, name='receita'),
]
