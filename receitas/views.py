from django.shortcuts import render, get_list_or_404, get_object_or_404
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
    receitas = get_list_or_404(
        Receita.objects.filter(
        categoria__id=categoria_id,
        publicado=True,
        ).order_by('-id')
    )


    return render(request, 'receitas/paginas/categoria.html', context={
        'receitas': receitas,
        'titulo': f'{receitas[0].categoria.nome} - Categoria | '
    })

def receita(request, id):
    receita = Receita.objects.filter(
            pk=id,
            publicado=True,
        ).order_by('-id').first()

    receita = get_object_or_404(
        Receita, 
        pk=id, 
        publicado=True
    )

    return render(request, 'receitas/paginas/receita-view.html', context={
        'receita': receita,
        'is_detail_page': True,
    })