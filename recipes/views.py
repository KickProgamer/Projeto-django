from django.shortcuts import render
from django.urls import HttpResponse


# Create your views here.
def home(request):
    numero = 'henrique'
    return render(request, 'home.html', context={
        'name': numero,
    })


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
