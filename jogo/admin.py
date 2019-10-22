from django.contrib import admin

# Register your models here.
from jogo.models import Jogo, Atleta, Adversario, JogoAtleta, Local, Noticia, Galeria, Conquista, ConquistaAtleta, \
    Fatura


class JogadorTabular(admin.TabularInline):
    model = JogoAtleta


class ConquistaTabular(admin.TabularInline):
    model = ConquistaAtleta


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    inlines = (JogadorTabular,)
    list_display = ['data', 'adversario', 'placar']

    def placar(self, obj):
        if obj.placar_adversario is not None:
            return f'{obj.placar_real} X {obj.placar_adversario}'
        return 'Jogo não realizado'

    placar.short_description = 'placar'


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_filter = ('nome',)
    list_display = ['nome', 'status']
    inlines = inlines = (ConquistaTabular,)


@admin.register(Adversario)
class AdversarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    pass


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    pass


def quitar_lote(modeladmin, request, queryset):
    queryset.update(valor_pago=50.0)

quitar_lote.short_description = "Quitar selecionadas"

@admin.register(Fatura)
class FaturaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'atleta', 'data_vencimento', 'valor_fatura', 'status')
    list_filter = ('descricao', 'categoria', 'tipo_fatura', 'atleta', 'valor_fatura')
    actions = [quitar_lote]