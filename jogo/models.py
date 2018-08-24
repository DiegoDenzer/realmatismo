from django.db import models, connection


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True)
    local_nascimento = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='atletas', null=True, blank=True)
    numero_camisa = models.CharField(max_length=50, null=True, blank=True)

    @property
    def gols(self):

        gols = 0
        cards = JogoAtleta.objects.filter(atleta=self)
        for card in cards:
            if card.gols is not None:
                gols = gols + card.gols
        return gols

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
    escudo_adversario = models.ImageField(default="/adversarios/sem_escudo.png", upload_to='adversarios', null=True,
                                          blank=True)

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

    def __str__(self):
        return self.adversario.nome

    class Meta:
        db_table = 'jogo'
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class JogoAtleta(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    gols = models.IntegerField(null=True, blank=True)
    asssitencia = models.IntegerField(null=True, blank=True)
    roubo_de_bola = models.IntegerField(null=True, blank=True)
    defesas = models.IntegerField(null=True, blank=True)
    minutos = models.IntegerField(null=True, blank=True)


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
