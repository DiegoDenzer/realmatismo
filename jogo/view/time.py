from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from jogo.models import Jogo, Atleta


class TimeDadosAPI(APIView):

    def get(self, request):

        data = Jogo.objects.dto_time()
        data['jogador_novo']: Atleta.objects.jogador_mais_novo()
        data['jogador_velho']: Atleta.objects.jogador_mais_velho()
        data['media_idade']: round(Atleta.objects.media_idade_atletas() / Atleta.objects.count(), 1)
        return Response(data)


class TimeList(View):

    template = 'jogo/time.html'

    def get(self, *args, **kwargs):
        data = Jogo.objects.dto_time()
        data['jogador_novo']: Atleta.objects.jogador_mais_novo()
        data['jogador_velho']: Atleta.objects.jogador_mais_velho()
        data['media_idade']: round(Atleta.objects.media_idade_atletas() / Atleta.objects.count(), 1)
        return render(self.request, self.template, data)
