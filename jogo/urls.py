from django.urls import path

from jogo.views import Home, ListaAtletas, AtletaDetail, JogoDetail, ListaJogos, ListaNoticias, NoticiaDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('atletas', ListaAtletas.as_view(), name='atletas'),
    path('atleta/<int:pk>', AtletaDetail.as_view(), name='atleta'),
    path('jogo/<int:pk>', JogoDetail.as_view(), name='jogo'),
    path('jogos', ListaJogos.as_view(), name='jogos'),
    path('noticias', ListaNoticias.as_view(), name='noticias'),
    path('noticia/<int:pk>', NoticiaDetail.as_view(), name='noticia'),
]
