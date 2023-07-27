from django.shortcuts import render, redirect
from .models import Texto


def home(request):
    return render(request, 'index.html')


def salvar(request):
    texto = request.POST['texto']
    Texto.objects.create(texto=texto)
    return redirect('home')


def textos_salvos(request):
    textos = Texto.objects.all()
    return render(request, 'textos_salvos.html', {'textos': textos})
