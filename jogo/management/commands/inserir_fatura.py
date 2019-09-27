from django.core.management import BaseCommand

from jogo.models import Atleta, Fatura
from datetime import date


class Command(BaseCommand):
    help = 'Criar faturas mensalidades real'

    def add_arguments(self, parser):
        parser.add_argument('operacao', nargs='+', type=str)

    def handle(self, *args, **options):
        for op in options['operacao']:
            if op == 'm':
                hoje = date.today()
                # 4 = 6
                if hoje.day > 11:
                    dia = 10 - hoje.day
                    fim = date.fromordinal(hoje.toordinal() + (hoje.day + dia))
                else:
                    fim = hoje

                atletas = Atleta.objects.filter(status_jogador='1')

                for atleta in atletas:
                    Fatura.objects.create(
                        descricao='Mensalidade {}/{}/{}'.format(fim.day, fim.month, fim.year),
                        atleta=atleta,
                        valor_fatura=50.0,
                        valor_pago=0,
                        tipo_fatura='R',
                        categoria='1',
                        data_vencimento=(fim)
                    )
