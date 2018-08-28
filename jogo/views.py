from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from jogo.models import Jogo, Atleta, Noticia, JogoAtleta


class Home(View):
    def get(self, *args, **kwargs):
        data= {}
        now = datetime.now()

        jogos_anteriores = Jogo.objects.order_by('-data').filter(data__lt=now)
        data['jogos_anteriores'] = jogos_anteriores[:3]

        proximos_jogos = Jogo.objects.order_by('data').filter(data__gte=now)
        data['proximos_jogos'] = proximos_jogos[:3]

        noticias = Noticia.objects.order_by('data_inclusao')
        data['noticias'] = noticias[:3]

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


class Estatisticas(View):
    template = 'jogo/estatistica.html'

    def get(self, *args, **kwargs):
        vitoria = 0
        derrota = 0
        empate = 0

        for jogo in Jogo.objects.filter(placar_real__isnull=False, placar_adversario__isnull=False):

            if jogo.placar_real > jogo.placar_adversario:
                vitoria += 1
            elif jogo.placar_adversario > jogo.placar_real:
                derrota += 1
            else:
                empate += 1

        jogadores = Atleta.objects.all()

        artilheiros = {}
        passadores = {}
        ladroes = {}
        defesas = {}
        participacoes = {}
        minutos = {}


        for jogador in jogadores:
            artilheiros[jogador] = jogador.gols
            passadores[jogador] = jogador.assistencia
            ladroes[jogador] = jogador.roubo
            defesas[jogador] = jogador.defesa
            participacoes[jogador] = jogador.jogos_realizados
            minutos[jogador] = jogador.minutos

        lista_artilheiros = sorted(artilheiros, key=artilheiros.__getitem__, reverse=True)
        lista_passsadores = sorted(passadores, key=passadores.__getitem__, reverse=True)
        lista_ladroes = sorted(ladroes, key=ladroes.__getitem__, reverse=True)
        lista_defesas = sorted(defesas, key=defesas.__getitem__, reverse=True)
        lista_jogos = sorted(participacoes, key=participacoes.__getitem__, reverse=True)
        lista_minutos = sorted(minutos, key=minutos.__getitem__, reverse=True)

        favor = Jogo.objects.all().aggregate(Sum('placar_real'))
        contra = Jogo.objects.all().aggregate(Sum('placar_adversario'))
        saldo = favor['placar_real__sum'] - contra['placar_adversario__sum']

        data = {
            # Dados Atletas...
            'artilharia': lista_artilheiros,
            'passadores': lista_passsadores,
            'ladroes': lista_ladroes,
            'defesas':  lista_defesas,
            'jogos_jogados': lista_jogos,
            'minutos': lista_minutos,
            #Dados Time...
            'gols_favor': favor['placar_real__sum'],
            'gols_contra':contra['placar_adversario__sum'],
            'vitoria': vitoria,
            'derrota':derrota,
            'empate': empate,
            'total': vitoria+derrota+empate,
            'saldo': saldo
        }
        return render(self.request, self.template, data)

