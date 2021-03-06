from datetime import datetime
from django.db import models
from django.db.models import Sum, Min, Max, Subquery



class JogoAtletaManager(models.Manager):

    def dto_atletas_jogo(self, jogo):
        result = []
        lista = self.filter(jogo=jogo)
        for item in lista:
            dto = {
                "nome": item.atleta.nome,
                "gols": item.gols,
                "assistencias": item.asssitencia,
                "defesas": item.defesas,
                "minutos": item.minutos
            }
            result.append(dto)
        return result


class AtletaManager(models.Manager):

    def jogador_mais_velho(self):
        velho = self.all().aggregate(Min('data_nascimento'))['data_nascimento__min']
        return self.get(data_nascimento=velho)

    def jogador_mais_novo(self):
        novo = self.all().aggregate(Max('data_nascimento'))['data_nascimento__max']
        return self.get(data_nascimento=novo)

    def media_idade_atletas(self):
        jogadores = self.all()
        media_idade = 0
        for jogador in jogadores:
            media_idade += jogador.idade
        return media_idade


    def home(self):
        lista = []

        dicionario = self.top_3_jogadores(1)
        for item in dicionario.items():

            a = item[1].pop()

            dto = {
                'tipo': item[0],
                'nome': a.nome,
                "atleta_id": a.id,
            }

            lista.append(dto)

        return lista


    def top_3_jogadores(self, qtd):

        jogadores = self.all()
        artilheiros = {}
        passadores = {}
        ladroes = {}
        defesas = {}
        participacoes = {}
        minutos = {}
        aproveitamento={}

        for jogador in jogadores:
            artilheiros[jogador] = jogador.gols
            passadores[jogador] = jogador.assistencia
            ladroes[jogador] = jogador.roubo
            defesas[jogador] = jogador.defesa
            participacoes[jogador] = jogador.jogos_realizados
            minutos[jogador] = jogador.minutos
            aproveitamento[jogador] = jogador.taxa_presente

        lista_artilheiros = sorted(artilheiros, key=artilheiros.__getitem__, reverse=True)
        lista_passsadores = sorted(passadores, key=passadores.__getitem__, reverse=True)
        lista_ladroes = sorted(ladroes, key=ladroes.__getitem__, reverse=True)
        lista_defesas = sorted(defesas, key=defesas.__getitem__, reverse=True)
        lista_jogos = sorted(participacoes, key=participacoes.__getitem__, reverse=True)
        lista_minutos = sorted(minutos, key=minutos.__getitem__, reverse=True)
        lista_aproveitamento = sorted(aproveitamento, key=aproveitamento.__getitem__, reverse=True)

        return {
            # Dados Atletas...
            'artilharia': lista_artilheiros[:qtd],
            'passadores': lista_passsadores[:qtd],
            'ladroes': lista_ladroes[:qtd],
            'defesas': lista_defesas[:qtd],
            'jogos_jogados': lista_jogos[:qtd],
            'minutos': lista_minutos[:qtd],
            'aproveitamento': lista_aproveitamento[:qtd],
        }

    def lista_por_categorias(self, tipo):

        jogadores = self.all()
        dicionario = {}

        for jogador in jogadores:
            if tipo == 'artilharia':
                dicionario[jogador] = jogador.gols
            elif tipo == 'assistencias':
                dicionario[jogador] = jogador.assistencia
            elif tipo == 'jogos-disputados':
                dicionario[jogador] = jogador.jogos_realizados
            elif tipo == 'defesas':
                dicionario[jogador] = jogador.defesa
            elif tipo == 'desempenho':
                dicionario[jogador] = jogador.taxa_presente
        lista = sorted(dicionario, key=dicionario.__getitem__, reverse=True)
        return lista


class JogoManager(models.Manager):
    ''' Manager para concentrar logicas de negocio dos jogos '''

    def dto_time(self):
        dados_time = self.dados_do_time()
        favor = self.gols_favor()
        contra = self.gols_contra()
        saldo = favor - contra

        data = {
            # Dados Time...
            'gols_favor': favor,
            'gols_contra': contra,
            'vitoria': dados_time['vitoria'],
            'derrota': dados_time['derrota'],
            'empate': dados_time['empate'],
            'total': dados_time['total'],
            'saldo': saldo,
            'media_gols': round(favor / dados_time['jogos'], 1),
            'media_sofridos': round(contra / dados_time['jogos'], 1),
            'maior_derrota': self.maior_derrota(),
            'maior_vitoria':self.maior_vitoria(),
            'performace': self.perfomace()
        }

        return data

    def gols_favor(self):
        return self.all().aggregate(Sum('placar_real'))['placar_real__sum']

    def gols_contra(self):
        return self.all().aggregate(Sum('placar_adversario'))['placar_adversario__sum']

    def maior_derrota(self):
        jogos_derrota = self.raw('''SELECT *,max(placar_adversario - placar_real) as maior from jogo''')
        for i in jogos_derrota:
            maior_derrota = f'{i.placar_real} X {i.placar_adversario} - {i.adversario}'
        return maior_derrota

    def maior_vitoria(self):
        jogos_vitoria = self.raw('''SELECT *,max(placar_real -placar_adversario) as maior from jogo''')
        for i in jogos_vitoria:
            maior_vitoria = f'{i.placar_real} X {i.placar_adversario} - {i.adversario}'
        return maior_vitoria

    def dados_do_time(self):
        vitoria = 0
        derrota = 0
        empate = 0
        jogos = self.filter(placar_real__isnull=False, placar_adversario__isnull=False)

        for jogo in jogos:
            if jogo.placar_real > jogo.placar_adversario:
                vitoria += 1
            elif jogo.placar_adversario > jogo.placar_real:
                derrota += 1
            else:
                empate += 1

        dados ={
            'jogos': jogos.count(),
            'total': vitoria + derrota + empate,
            'vitoria': vitoria,
            'derrota': derrota,
            'empate': empate
        }
        return dados

    def sequencia(self):
        data = None
        now = datetime.now()
        jogos_anteriores = self.order_by('-data') \
            .filter(data__lt=now, placar_real__isnull=False, placar_adversario__isnull=False)
        for jogo in jogos_anteriores:
            if jogo.placar_adversario > jogo.placar_real:
                data = jogo.data
                break
        return self.filter(data__gt=data, placar_real__isnull=False, placar_adversario__isnull=False).count()

    def perfomace(self):
        now = datetime.now()
        jogos_anteriores = self.order_by('-data') \
            .filter(data__lt=now, placar_real__isnull=False, placar_adversario__isnull=False)
        performace = []
        for jogo in jogos_anteriores[:5]:
            if jogo.placar_real > jogo.placar_adversario:
                performace.append('V')
            elif jogo.placar_adversario > jogo.placar_real:
                performace.append('D')
            else:
                performace.append('E')
        return performace

    def perfomace2(self):
        now = datetime.now()
        jogos_anteriores = self.order_by('-data') \
            .filter(data__lt=now, placar_real__isnull=False, placar_adversario__isnull=False)

        pts = 0
        possiveis = 0
        for jogo in jogos_anteriores:
            possiveis += 3
            if jogo.placar_real > jogo.placar_adversario:
                pts += 3
            elif jogo.placar_adversario > jogo.placar_real:
                pts += 0
            else:
                pts += 1
        if pts > 0:
            return round(((pts/possiveis) * 100), 2)
        else:
            return 0
