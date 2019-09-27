from django.views.generic import DetailView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class JogosApi(APIView):

    def get(self, request, format=None):
        jogos = Jogo.objects.all()
        serializer = JogoSerializer(jogos, many=True)
        return Response(serializer.data)

