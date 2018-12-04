from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Sum, Min, Max, Count
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from jogo.models import Jogo, Atleta, Noticia, JogoAtleta, Galeria


class Home(View):
    def get(self, *args, **kwargs):
        data = {}
        now = datetime.now()
        jogos_anteriores = Jogo.objects.order_by('-data').filter(data__lt=now)
        proximos_jogos = Jogo.objects.order_by('data').filter(data__gte=now)
        noticias = Noticia.objects.order_by('-data_inclusao')

        data ={
            'jogos_anteriores': jogos_anteriores[:1],
            'proximos_jogos': proximos_jogos[:1],
            'noticias': noticias[:1],
            'performace': Jogo.objects.perfomace(),
            'teste': Jogo.objects.perfomace2()
        }


        return render(self.request, 'jogo/home.html', data)


class ListaAtletas(ListView):
    template_name = 'jogo/atletas.html'
    model = Atleta
    context_object_name = 'atletas'

    def get_queryset(self):
        return Atleta.objects.order_by('nome')


class ListaNoticias(ListView):
    template_name = 'jogo/noticias.html'
    model = Noticia
    context_object_name = 'noticias'


class NoticiaDetail(DetailView):
    context_object_name = 'noticia'
    model = Noticia
    template_name = 'jogo/noticia.html'


class AtletaDetail(DetailView):
    context_object_name = 'atleta'
    model = Atleta
    template_name = 'jogo/atleta_detalhe.html'


class JogoDetail(DetailView):
    context_object_name = 'jogo'
    model = Jogo
    template_name = 'jogo/jogo_detalhe.html'


class ListaJogos(ListView):
    context_object_name = 'jogos'
    model = Jogo
    paginate_by = 5
    queryset = Jogo.objects.order_by('-data')
    template_name = 'jogo/jogos.html'


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


class Roubadas(View):
    template = 'jogo/roubadas.html'

    def get(self, *args, **kwargs):
        jogadores = Atleta.objects.all()
        dic = {}
        for jogador in jogadores:
            dic[jogador] = jogador.roubo
        lista = sorted(dic, key=dic.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista})


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


class ListaAtletas(ListView):
    template_name = 'jogo/atletas.html'
    model = Atleta
    context_object_name = 'atletas'


class Galeria(ListView):
    template_name = 'jogo/galeria.html'
    model = Galeria
    context_object_name = 'fotos'


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