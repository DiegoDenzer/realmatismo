from django.contrib import admin

# Register your models here.
from jogo.models import Jogo, Atleta

class JogoAdmin(admin.ModelAdmin):
   pass

class AtletaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Jogo, JogoAdmin)
admin.site.register(Atleta, AtletaAdmin)