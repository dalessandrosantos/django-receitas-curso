from django.shortcuts import render

def home(request):
    return render(request, 'receitas/paginas/home.html')

def receita(request, id):
    context = {
        'name': 'Dalessandro'
    }
    return render(request, 'receitas/paginas/receita-view.html', context)