import imp

from django.http import HttpResponse
from django.shortcuts import render  # Alterado


def home(request):
    return render(request, 'recipes/home.html')  # alterado


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
