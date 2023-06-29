from django.shortcuts import render
from django.http import HttpResponse
from .models import Texto
import json
# Create your views here.
def home(request):
    return render(request, 'index.html')

def salvar(request):
    dados = json.loads(request.body)
    texto = dados['texto']

    Texto.objects.create(texto=texto)
    resposta = {'mensagem':'Texto salvo com Sucesso'}
    resposta = json.dumps(resposta)
    return HttpResponse(resposta)

def textos_salvos(request):
    textos = Texto.objects.all()
    return render(request,'textos_salvos.html', {'textos': textos})