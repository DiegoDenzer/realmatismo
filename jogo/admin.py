from django.contrib import admin

# Register your models here.
from jogo.models import Jogo, Atleta, Adversario, JogoAtleta, Local


class JogadorTabular(admin.TabularInline):
    model = JogoAtleta

class JogoAdmin(admin.ModelAdmin):
   inlines = (JogadorTabular,)

class AtletaAdmin(admin.ModelAdmin):
    pass

class AdversarioAdmin(admin.ModelAdmin):
    pass

class LocalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Jogo, JogoAdmin)
admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Adversario, AdversarioAdmin)
admin.site.register(Local, LocalAdmin)