from django.db.models import Max, Sum
from django.shortcuts import render
from django.views import View

from jogo.models import Fatura


class CaixinhaView(View):
    template = 'jogo/caixinha.html'

    def get(self, request ,*args, **kwargs):
        fat = Fatura.objects.all()
        valor_receita = Fatura.objects.filter(tipo_fatura='R').aggregate(Sum('valor_pago')).get('valor_pago__sum')
        valor_despesa = Fatura.objects.filter(tipo_fatura='D').aggregate(Sum('valor_pago')).get('valor_pago__sum')
        return render(self.request, self.template, {'receita': valor_receita, 'faturas': fat, 'despesa': valor_despesa,})


