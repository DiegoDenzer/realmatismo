from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from jogo.models import Jogo, Atleta


class Home(View):
    def get(self, *args, **kwargs):
        jogos = Jogo.objects.order_by('-data')
        return render(self.request, 'jogo/home.html', {'jogos': jogos})

class ListaAtletas(ListView):
    template_name = 'jogo/atletas.html'
    model = Atleta
    context_object_name = 'atletas'

class AtletaDetail(DetailView):
    context_object_name = 'atleta'
    model = Atleta
    template_name = 'jogo/atleta_detalhe.html'

class JogoDetail(DetailView):
    context_object_name = 'jogo'
    model = Jogo
    template_name = 'jogo/jogo_detalhe.html'

class ListaJogos(View):
    def get(self, *args, **kwargs):
        jogos = Jogo.objects.order_by('-data')
        return render(self.request, 'jogo/jogos.html', {'jogos': jogos})