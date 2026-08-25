from django.shortcuts import render

def home(request):
    return render(request, 'receitas/paginas/home.html')

def receitas(request):
    return render(request, 'receitas/paginas/receita-view.html')