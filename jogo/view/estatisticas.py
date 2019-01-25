from django.shortcuts import render
from django.views import View

from jogo.models import Atleta


class Estatisticas(View):
    template = 'jogo/estatistica.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template, Atleta.objects.top_3_jogadores())


class Artilheiros(View):
    template = 'jogo/artilharia.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template, {'lista': Atleta.objects.lista_por_categorias('artilharia')})


class Assistencias(View):
    template = 'jogo/assistencias.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template, {'lista': Atleta.objects.lista_por_categorias('assistencias')})


class Desempenho(View):
    template = 'jogo/desempenho.html'
    def get(self, request):
        return render(request, self.template , {'lista': Atleta.objects.lista_por_categorias('desempenho')})


class Defesas(View):
    template = 'jogo/defesas.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template, {'lista': Atleta.objects.lista_por_categorias('defesas')})


class JogosDisputados(View):
    template = 'jogo/jogos-disputados.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template, {'lista': Atleta.objects.lista_por_categorias('jogos-disputados')})


class Minutos(View):
    template = 'jogo/minutos.html'

    def get(self, *args, **kwargs):
        jogadores = Atleta.objects.all()
        dic = {}
        for jogador in jogadores:
            dic[jogador] = jogador.minutos
        lista = sorted(dic, key=dic.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista})