from django.shortcuts import render

def home(request):
    return render(request, 'receitas/paginas/home.html')
