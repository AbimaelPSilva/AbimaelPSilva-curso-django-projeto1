import imp

from django.shortcuts import render  # Alterado


def home(request):
    return render(request, 'recipes/pages/home.html')  # alterado
