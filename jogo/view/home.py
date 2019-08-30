from datetime import datetime

from django.shortcuts import render
from django.views import View

from jogo.models import Jogo, Noticia

class Home(View):

    def get(self, *args, **kwargs):
        data = {}
        now = datetime.now()
        jogos_anteriores = Jogo.objects.order_by('-data').filter(data__lt=now)
        proximos_jogos = Jogo.objects.order_by('data').filter(data__gte=now)
        noticias = Noticia.objects.order_by('-data_inclusao')
        string = ''
        if proximos_jogos.count() > 0:
            te = Jogo.objects.filter(adversario=proximos_jogos[0].adversario).order_by('-data')

            if te.count() > 1:
                if te[1].placar_real > te[1].placar_adversario:
                    string = f'No Último confronto entre as duas equipes vitória do Realmatismo pelo placar de: {te[1].placar_real} x {te[1].placar_adversario}'
                elif te[1].placar_real < te[1].placar_adversario:
                    string = f'No Último confronto entre as duas equipes derrota do Realmatismo pelo placar de: {te[1].placar_real} x {te[1].placar_adversario}'
                elif te[1].placar_real == te[1].placar_adversario:
                    string = f'No Último confronto entre as duas equipes empate pelo placar de: {te[1].placar_real} x {te[1].placar_adversario}'
            else:
                string= 'Primeiro jogo entre as duas equipes'

        data ={
            'detalhes_ultimo': string,
            'jogos_anteriores': jogos_anteriores[:1],
            'proximos_jogos': proximos_jogos[:1],
            'noticias': noticias[:1],
            'performace': Jogo.objects.perfomace(),
            'teste': Jogo.objects.perfomace2(),
            'seguencia': Jogo.objects.sequencia()
        }

        return render(self.request, 'jogo/home.html', data)