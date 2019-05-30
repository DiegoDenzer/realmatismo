from django.contrib import admin

# Register your models here.
from jogo.models import Jogo, Atleta, Adversario, JogoAtleta, Local, Noticia, Galeria, Conquista, ConquistaAtleta


class JogadorTabular(admin.TabularInline):
    model = JogoAtleta

class ConquistaTabular(admin.TabularInline):
    model = ConquistaAtleta

class JogoAdmin(admin.ModelAdmin):
   inlines = (JogadorTabular,)
   list_display = ['data', 'adversario', 'placar']

   def placar(self, obj):
       if obj.placar_adversario is not None:
           return f'{obj.placar_real} X {obj.placar_adversario}'

       return 'Jogo não realizado'

   placar.short_description = 'placar'


class AtletaAdmin(admin.ModelAdmin):
    inlines = inlines = (ConquistaTabular,)


class AdversarioAdmin(admin.ModelAdmin):
    pass


class LocalAdmin(admin.ModelAdmin):
    pass


class NoticiaAdmin(admin.ModelAdmin):
    pass


class GaleriaAdmin(admin.ModelAdmin):
    pass

class ConquistaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Jogo, JogoAdmin)
admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Adversario, AdversarioAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Conquista, ConquistaAdmin)