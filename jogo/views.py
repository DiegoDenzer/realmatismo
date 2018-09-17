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


class ListaJogos(View):

    def get(self, *args, **kwargs):
        jogos = Jogo.objects.order_by('-data')
        paginator = Paginator(jogos, 3)
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(self.request, 'jogo/jogos.html', {'jogos': contacts})


class Estatisticas(View):
    template = 'jogo/estatistica.html'

    def get(self, *args, **kwargs):

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

        data = {
            # Dados Atletas...
            'artilharia': lista_artilheiros[:3],
            'passadores': lista_passsadores[:3],
            'ladroes': lista_ladroes[:3],
            'defesas': lista_defesas[:3],
            'jogos_jogados': lista_jogos[:3],
            'minutos': lista_minutos[:3],

        }
        return render(self.request, self.template, data)


class Artilheiros(View):
    template = 'jogo/artilharia.html'

    def get(self, *args, **kwargs):
        jogadores = Atleta.objects.all()
        artilheiros = {}
        for jogador in jogadores:
            artilheiros[jogador] = jogador.gols
        lista_artilheiros = sorted(artilheiros, key=artilheiros.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista_artilheiros})


class Assistencias(View):
    template = 'jogo/assistencias.html'

    def get(self, *args, **kwargs):
        jogadores = Atleta.objects.all()
        assist = {}
        for jogador in jogadores:
            assist[jogador] = jogador.assistencia
        lista = sorted(assist, key=assist.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista})


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
        jogadores = Atleta.objects.all()
        dic = {}
        for jogador in jogadores:
            dic[jogador] = jogador.defesa
        lista = sorted(dic, key=dic.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista})


class JogosDisputados(View):
    template = 'jogo/jogos-disputados.html'

    def get(self, *args, **kwargs):
        jogadores = Atleta.objects.all()
        dic = {}
        for jogador in jogadores:
            dic[jogador] = jogador.jogos_realizados
        lista = sorted(dic, key=dic.__getitem__, reverse=True)
        return render(self.request, self.template, {'lista': lista})


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
        vitoria = 0
        derrota = 0
        empate = 0
        media_sofridos = 0
        jogos = Jogo.objects.filter(placar_real__isnull=False, placar_adversario__isnull=False)
        for jogo in jogos:

            media_sofridos += jogo.placar_adversario

            if jogo.placar_real > jogo.placar_adversario:
                vitoria += 1
            elif jogo.placar_adversario > jogo.placar_real:
                derrota += 1
            else:
                empate += 1

        favor = Jogo.objects.all().aggregate(Sum('placar_real'))['placar_real__sum']
        contra = Jogo.objects.all().aggregate(Sum('placar_adversario'))['placar_adversario__sum']
        saldo = favor - contra

        maior_derrota = ''
        maior_vitoria = ''
        jogos_derrota = Jogo.objects.raw('''SELECT *,max(placar_adversario - placar_real) as maior from jogo''')
        jogos_vitoria = Jogo.objects.raw('''SELECT *,max(placar_real -placar_adversario) as maior from jogo''')

        for i in jogos_derrota:
            maior_derrota = f'{i.placar_real} X {i.placar_adversario} - {i.adversario}'

        for i in jogos_vitoria:
            maior_vitoria = f'{i.placar_real} X {i.placar_adversario} - {i.adversario}'



        # Estatisticas e curiosidades...
        velho = Atleta.objects.all().aggregate(Min('data_nascimento'))['data_nascimento__min']
        jogador_velho = Atleta.objects.get(data_nascimento=velho)

        novo = Atleta.objects.all().aggregate(Max('data_nascimento'))['data_nascimento__max']
        jogador_novo = Atleta.objects.get(data_nascimento=novo)

        jogadores = Atleta.objects.all()
        media_idade = 0

        for jogador in jogadores:
            media_idade += jogador.idade

        now = datetime.now()
        jogos_anteriores = Jogo.objects.order_by('-data')\
                                       .filter(data__lt=now, placar_real__isnull=False, placar_adversario__isnull=False)

        performace = []
        for jogo in jogos_anteriores[:5]:

            if jogo.placar_real > jogo.placar_adversario:
                performace.append('V')
            elif jogo.placar_adversario > jogo.placar_real:
                performace.append('D')
            else:
                performace.append('E')

        data = {
        # Dados Time...
            'gols_favor': favor,
            'gols_contra': contra,
            'vitoria': vitoria,
            'derrota': derrota,
            'empate': empate,
            'total': vitoria + derrota + empate,
            'saldo': saldo,
            'media_gols': round(favor / jogos.count(), 1),
            'media_sofridos': round(contra / jogos.count(), 1),
        # Coisas alway
            'jogador_novo': jogador_novo,
            'jogador_velho': jogador_velho,
            'media_idade': round(media_idade / jogadores.count(), 1),
            'maior_derrota': maior_derrota,
            'maior_vitoria': maior_vitoria,
            'performace': performace
        }
        return render(self.request, self.template, data)