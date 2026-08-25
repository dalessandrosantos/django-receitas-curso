from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('receita-view/', views.receitas, name='receitas'),
]
