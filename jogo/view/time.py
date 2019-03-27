from django.shortcuts import render
from django.views import View

from jogo.models import Jogo, Atleta


class TimeList(View):

    template = 'jogo/time.html'

    def get(self, *args, **kwargs):
        # Dados Time...
        dados_time = Jogo.objects.dados_do_time()
        favor = Jogo.objects.gols_favor()
        contra = Jogo.objects.gols_contra()
        saldo = favor - contra
        # Estatisticas e curiosidades...
        jogadores = Atleta.objects.all()
        media_idade = Atleta.objects.media_idade_atletas()

        data = {
            # Dados Time...
            'gols_favor': favor,
            'gols_contra': contra,
            'vitoria': dados_time['vitoria'],
            'derrota': dados_time['derrota'],
            'empate': dados_time['empate'],
            'total': dados_time['total'],
            'saldo': saldo,
            'media_gols': round(favor / dados_time['jogos'], 1),
            'media_sofridos': round(contra / dados_time['jogos'], 1),
            # Coisas alway
            'jogador_novo': Atleta.objects.jogador_mais_novo(),
            'jogador_velho': Atleta.objects.jogador_mais_velho(),
            'media_idade': round(media_idade / jogadores.count(), 1),
            'maior_derrota': Jogo.objects.maior_derrota(),
            'maior_vitoria': Jogo.objects.maior_vitoria(),
            'performace': Jogo.objects.perfomace()
        }
        return render(self.request, self.template, data)