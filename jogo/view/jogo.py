from datetime import datetime

from django.views.generic import DetailView, ListView
from rest_framework import generics, viewsets


from jogo.models import Jogo
from jogo.serializer import JogoSerializer


class JogoDetail(DetailView):
    context_object_name = 'jogo'
    model = Jogo
    template_name = 'jogo/jogo_detalhe.html'


class ListaJogos(ListView):
    context_object_name = 'jogos'
    model = Jogo
    paginate_by = 8
    queryset = Jogo.objects.order_by('-data')
    template_name = 'jogo/jogos.html'


class ProximosJogosAPI(viewsets.ModelViewSet):

    queryset = Jogo.objects.order_by('data').filter(data__gte=datetime.now())
    serializer_class = JogoSerializer


class JogosAnterioresAPI(viewsets.ModelViewSet):

    queryset = Jogo.objects.order_by('-data').filter(data__lt=datetime.now())
    serializer_class = JogoSerializer


