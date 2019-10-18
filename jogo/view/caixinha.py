from django.shortcuts import render
from django.views import View

from jogo.models import  Fatura


class CaixinhaView(View):
    template = 'jogo/caixinha.html'

    def get(self, *args, **kwargs):
        fat = Fatura.objects.all()
        valor_pago = 0
        for f in fat:
            if f.valor_pago is not None:
                valor_pago += f.valor_pago
        return render(self.request, self.template, {'valor': valor_pago, 'faturas': fat})


