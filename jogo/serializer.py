from rest_framework import serializers

from jogo.models import Jogo, Adversario, Atleta


class AdversarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adversario
        fields = ('nome', )


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        depth = 1
        fields = ('id', 'data', 'placar_real', 'placar_adversario', 'adversario', 'local', 'resumo')


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = ('id', 'nome', 'gols')