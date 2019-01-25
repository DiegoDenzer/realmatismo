from django.views import View


class ContatoView(View):
    template = 'jogo/contato.html'

    def get(self, request):
        pass