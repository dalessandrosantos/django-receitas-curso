from django.shortcuts import render
from utils.receitas.factory import make_recipe
from .models import Receita

def home(request):
    receitas = Receita.objects.filter(
        publicado=True
    ).order_by('-id')
    return render(request, 'receitas/paginas/home.html', context={
        'receitas': receitas,
    })

def categoria(request, categoria_id):
    receitas = Receita.objects.filter(
        categoria__id=categoria_id,
        publicado=True
    ).order_by('-id')
    return render(request, 'receitas/paginas/categoria.html', context={
        'receitas': receitas,
    })

def receita(request, id):
    return render(request, 'receitas/paginas/receita-view.html', context={
        'receita': make_recipe(),
        'is_detail_page': True,
    })