from django.urls import path

from jogo.views import Home, ListaAtletas, AtletaDetail, JogoDetail, ListaJogos, ListaNoticias, NoticiaDetail, \
    Estatisticas, Artilheiros, Assistencias, Roubadas, Defesas, Minutos, JogosDisputados, Galeria

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
    path('roubadas', Roubadas.as_view(), name='roubadas'),
    path('minutos', Minutos.as_view(), name='minutos'),
    path('jogos-jogados', JogosDisputados.as_view(), name='jogos-jogados'),

    path('galeria', Galeria.as_view(), name='galeria'),

]
