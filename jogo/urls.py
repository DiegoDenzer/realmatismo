from django.urls import path

from jogo.views import Home, ListaAtletas, AtletaDetail, JogoDetail, ListaJogos

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('atletas', ListaAtletas.as_view(), name='atletas'),
    path('atleta/<int:pk>', AtletaDetail.as_view(), name='atleta'),
    path('jogo/<int:pk>', JogoDetail.as_view(), name='jogo'),
    path('jogos', ListaJogos.as_view(), name='jogos'),
]
