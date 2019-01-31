from django.views.generic import DetailView, ListView

from jogo.models import Jogo


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
