from django.urls import path

from jogo.view.atletas import ListaAtletas, AtletaDetail
from jogo.view.contato import ContatoView
from jogo.view.estatisticas import Estatisticas, Artilheiros, Assistencias, Defesas, Desempenho, Minutos, \
    JogosDisputados
from jogo.view.home import Home
from jogo.view.jogo import JogoDetail, ListaJogos
from jogo.view.time import TimeList
from jogo.views import  ListaNoticias, NoticiaDetail, Galeria,  AdversariosView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('atletas', ListaAtletas.as_view(), name='atletas'),
    path('atleta/<int:pk>', AtletaDetail.as_view(), name='atleta'),
    path('jogo/<int:pk>', JogoDetail.as_view(), name='jogo'),
    path('jogos', ListaJogos.as_view(), name='jogos'),
    path('noticias', ListaNoticias.as_view(), name='noticias'),
    path('noticia/<int:pk>', NoticiaDetail.as_view(), name='noticia'),
    path('estatistica', Estatisticas.as_view(), name='estatistica'),

    path('artilharia', Artilheiros.as_view(), name='artilharia'),
    path('assistencias', Assistencias.as_view(), name='assistencias'),
    path('defesas', Defesas.as_view(), name='defesas'),
    path('desempenho', Desempenho.as_view(), name='desempenho'),
    path('minutos', Minutos.as_view(), name='minutos'),
    path('jogos-jogados', JogosDisputados.as_view(), name='jogos-jogados'),

    path('galeria', Galeria.as_view(), name='galeria'),
    path('time', TimeList.as_view(), name='time'),
    path('adversarios', AdversariosView.as_view(), name='adversarios'),

    path('contato', ContatoView.as_view(), name='contato'),


]
