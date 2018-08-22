from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from jogo.models import Jogo, Atleta, Noticia


class Home(View):
    def get(self, *args, **kwargs):
        data= {}
        now = datetime.now()

        jogos_anteriores = Jogo.objects.order_by('-data').filter(data__lt=now)
        data['jogos_anteriores'] = jogos_anteriores

        proximos_jogos = Jogo.objects.order_by('data').filter(data__gte=now)
        data['proximos_jogos'] = proximos_jogos

        noticias = Noticia.objects.order_by('data_inclusao')
        data['noticias'] = noticias

        return render(self.request, 'jogo/home.html', data)

class ListaAtletas(ListView):
    template_name = 'jogo/atletas.html'
    model = Atleta
    context_object_name = 'atletas'

class ListaNoticias(ListView):
    template_name = 'jogo/noticias.html'
    model = Noticia
    context_object_name = 'noticias'

class NoticiaDetail(DetailView):
    context_object_name = 'noticia'
    model = Atleta
    template_name = 'jogo/noticia.html'


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