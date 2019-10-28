from django.urls import path, include
from rest_framework import routers

from jogo import views
from jogo.view.atletas import ListaAtletas, AtletaDetail
from jogo.view.caixinha import CaixinhaView
from jogo.view.contato import ContatoView
from jogo.view.estatisticas import Estatisticas, Artilheiros, Assistencias, Defesas, Desempenho, Minutos, \
    JogosDisputados, HomeEstatisticasAPI
from jogo.view.home import Home
from jogo.view.jogo import JogoDetail, ListaJogos, ProximosJogosAPI, JogosAnterioresAPI, JogoAtletasAPI
from jogo.view.time import TimeList, TimeDadosAPI
from jogo.views import ListaNoticias, NoticiaDetail, Galeria,  AdversariosView


router = routers.DefaultRouter()
router.register(r'proximos-jogos', ProximosJogosAPI)
router.register(r'jogos-anteriores', JogosAnterioresAPI)

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

    path('caixa', CaixinhaView.as_view(), name='contato'),

    #API
    path('api/', include(router.urls)),
    path('api/est-home', HomeEstatisticasAPI.as_view(), name="estatisticas-home"),
    path('api/jogo-atleta/<int:jogo>', JogoAtletasAPI.as_view(), name="jogo-atleta"),
    path('api/dados-time', TimeDadosAPI.as_view(), name="dados-time"),

]
