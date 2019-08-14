from django.db.models.signals import post_save

__author__ = 'Diego Denzer'
from django.db import models, connection
from datetime import date

from jogo.manager import JogoManager, AtletaManager

STATUS = (
    ('1', 'Elenco Principal'),
    ('2', 'Departamento Médico'),
    ('3', 'Aposentado'),
    ('4', 'Convidado'),
    ('5', 'Suspenso'),
)

TIPO_CONQUISTA = (
    ('1', 'Gols'),
    ('2', 'Assitencias'),
    ('3', 'Jogos'),
    ('4', 'Defesas'),
    ('5', 'Hat-Trick'),
)


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True)
    local_nascimento = models.CharField(max_length=50)
    imagem = models.ImageField(default="/adversarios/sem-foto.png", upload_to='adversarios', null=True, blank=True)
    numero_camisa = models.CharField(max_length=50, null=True, blank=True)
    status_jogador = models.CharField(max_length=2, choices=STATUS, default='1')

    objects = AtletaManager()

    @property
    def status(self):
        if self.status_jogador == '1':
            return STATUS[0][1]
        elif self.status_jogador == '2':
            return STATUS[1][1]
        elif self.status_jogador == '3':
            return STATUS[2][1]
        elif self.status_jogador == '4':
            return STATUS[3][1]
        elif self.status_jogador == '5':
            return STATUS[4][1]
        else:
            return 'Sem Status'

    @property
    def idade(self):
        hoje = date.today()
        try:
            aniversario = self.data_nascimento.replace(year=hoje.year)
        except ValueError:  # Fevereiro 29
            aniversario = self.data_nascimento.replace(year=hoje.year, month=hoje.month + 1, day=1)
        if aniversario > hoje:
            return hoje.year - self.data_nascimento.year - 1
        else:
            return hoje.year - self.data_nascimento.year

    @property
    def taxa_presente(self):
        jogos = JogoAtleta.objects.filter(atleta=self)
        pts = 0

        if jogos is None:
            return 0

        possiveis = 3 * jogos.count()

        if possiveis == 0:
            return 0

        for j in jogos:
            if j.jogo.placar_real > j.jogo.placar_adversario:
                pts += 3
            elif j.jogo.placar_real < j.jogo.placar_adversario:
                pts += 0
            else:
                pts += 1

        return round((pts/possiveis) * 100, 2)

    @property
    def gols(self):
        gols = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.gols is not None:
                gols = gols + card.gols
        return gols

    @property
    def media_gols(self):
        g = self.gols
        p = JogoAtleta.objects.filter(atleta=self).count()
        if g > 0:
            return g/p
        else:
            return 0

    @property
    def minutos(self):
        minutos = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.minutos is not None:
                minutos = minutos + card.minutos
        return minutos

    @property
    def assistencia(self):
        assistencia = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.asssitencia is not None:
                assistencia = assistencia + card.asssitencia
        return assistencia

    @property
    def media_assistencia(self):
        a = self.assistencia
        p = JogoAtleta.objects.filter(atleta=self).count()
        if a > 0:
            return a / p
        else:
            return 0

    @property
    def roubo(self):
        r_b = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.roubo_de_bola is not None:
                r_b += card.roubo_de_bola
        return r_b

    @property
    def defesa(self):
        defesa = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.defesas is not None:
                defesa += card.defesas
        return defesa

    @property
    def media_defesa(self):
        d = self.defesa
        p = JogoAtleta.objects.filter(atleta=self).count()
        if d > 0:
            return d / p
        else:
            return 0

    @property
    def jogos_realizados(self):
        return JogoAtleta.objects.filter(atleta=self).count()

    class Meta:
        db_table = 'atleta'
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"

    def __str__(self):
        return self.nome + " " + self.sobrenome


class Adversario(models.Model):
    nome = models.CharField(max_length=50)
    escudo_adversario = models.ImageField(default="/adversarios/sem_escudo.png", upload_to='adversarios',
                                          null=True,blank=True)
    telefone = models.CharField(default='', max_length=14)

    @property
    def jogos(self):

        jogos = Jogo.objects.filter(adversario=self, placar_real__isnull=False, placar_adversario__isnull=False).count()
        return jogos;

    @property
    def vitoria(self):
        jogos = Jogo.objects.filter(adversario=self, placar_real__isnull=False, placar_adversario__isnull=False)
        v= 0
        for j in jogos:
            if j.placar_real < j.placar_adversario:
                v += 1
        return v;

    @property
    def derrota(self):
        jogos = Jogo.objects.filter(adversario=self, placar_real__isnull=False, placar_adversario__isnull=False)
        d = 0
        for j in jogos:
            if j.placar_real > j.placar_adversario:
                d += 1
        return d;

    @property
    def empate(self):
        jogos = Jogo.objects.filter(adversario=self, placar_real__isnull=False, placar_adversario__isnull=False)
        d = 0
        for j in jogos:
            if j.placar_real == j.placar_adversario:
                d += 1
        return d;

    class Meta:
        db_table = 'adversario'
        verbose_name = "Adversário"
        verbose_name_plural = "Adversários"

    def __str__(self):
        return self.nome


class Local(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'local'
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    adversario = models.ForeignKey(Adversario, on_delete=models.CASCADE)
    data = models.DateTimeField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    placar_real = models.IntegerField(null=True, blank=True)
    placar_adversario = models.IntegerField(null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)

    objects = JogoManager()

    def __str__(self):
        return self.adversario.nome

    @property
    def relacionados(self):
        lista = self.jogadores.all()
        final = []
        final.append(lista.first())
        for dado in lista:
            if not dado.atleta in final:
               final.append(dado.atleta)
        return final

    class Meta:
        ordering = ('-data',)
        db_table = 'jogo'
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class JogoAtleta(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='jogadores')
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    gols = models.IntegerField(null=True, blank=True)
    asssitencia = models.IntegerField(null=True, blank=True)
    roubo_de_bola = models.IntegerField(null=True, blank=True)
    defesas = models.IntegerField(null=True, blank=True)
    minutos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.atleta.nome

    class Meta:
        db_table = 'jogo_x_atleta'
        verbose_name = "JogoAtleta"
        verbose_name_plural = "JogoAtletas"


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    corpo = models.TextField()
    data_inclusao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'noticia'
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"


class Galeria(models.Model):

    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='galeria')

    class Meta:
        db_table = 'galeria'
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria"


class Conquista(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.PositiveIntegerField(default=0)
    tipo = models.CharField(choices=TIPO_CONQUISTA, max_length=2)
    imagem = models.ImageField(default="/adversarios/sem_escudo.png", upload_to='adversarios', null=True, blank=True)


    class Meta:
        verbose_name = "Conquista"
        verbose_name_plural = "Conquistas"

    def __str__(self):
        return self.nome


class ConquistaAtleta(models.Model):
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, related_name='conquistas')
    data_conquista = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.conquista.nome

def cria_objeto(conquista, jogador):
    ConquistaAtleta.objects.create(conquista=conquista, atleta=jogador)


def validar_conquista(conquista, jogador):
    if conquista.tipo == '1' and jogador.gols >= conquista.valor:
        cria_objeto(conquista, jogador)
    elif conquista.tipo == '2' and jogador.assistencia >= conquista.valor:
        cria_objeto(conquista, jogador)
    elif conquista.tipo == '3' and jogador.jogos_realizados >= conquista.valor:
        cria_objeto(conquista, jogador)
    elif conquista.tipo == '4' and jogador.defesa >= conquista.valor:
        cria_objeto(conquista, jogador)


def cria_conquista(sender, instance, created, **kwargs):
    if not created:
        jogadores = instance.jogadores.all()
        lista_conquista = Conquista.objects.all()
        for jogador in jogadores:
            conquistas_jogador = jogador.atleta.conquistas.all()
            teste = []
            for cj in conquistas_jogador:
                teste.append(cj.conquista)

            for conquista in lista_conquista:
                if conquista not in teste:
                    validar_conquista(conquista, jogador.atleta)

post_save.connect(cria_conquista, sender=Jogo)