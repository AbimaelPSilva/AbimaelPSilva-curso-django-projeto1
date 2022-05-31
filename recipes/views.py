from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)], # list comprehension que gera 10 receitas
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(), # Gera um nome
        'is_detail_page' : True, # criamos uma variavel que é igual a True
    })
