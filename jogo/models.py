from django.db import models


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True)
    local_nascimento = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='atletas', null=True, blank=True)

    class Meta:
        db_table = 'atleta'
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"

    def __str__(self):
        return self.nome + " " + self.sobrenome


class Jogo(models.Model):
    adversario = models.CharField(max_length=50)
    data = models.DateField()
    local = models.CharField(max_length=50)
    arbitragem = models.CharField(max_length=80, null=True, blank=True)
    escudo_adversario = models.ImageField(default="comuns/sem_escudo.png", upload_to='jogos', null=True, blank=True)
    placar_real = models.IntegerField(null=True, blank=True)
    placar_adversario = models.IntegerField(null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.adversario

    class Meta:
        db_table = 'jogo'
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class JogoAtleta(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta,  on_delete=models.CASCADE)