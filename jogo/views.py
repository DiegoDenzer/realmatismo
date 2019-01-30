from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Sum, Min, Max, Count
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from jogo.models import Jogo, Atleta, Noticia, JogoAtleta, Galeria, Adversario

class ListaNoticias(ListView):
    template_name = 'jogo/noticias.html'
    model = Noticia
    context_object_name = 'noticias'


class NoticiaDetail(DetailView):
    context_object_name = 'noticia'
    model = Noticia
    template_name = 'jogo/noticia.html'


class Galeria(ListView):
    template_name = 'jogo/galeria.html'
    model = Galeria
    context_object_name = 'fotos'


class AdversariosView(ListView):
    template_name = 'jogo/adversarios.html'
    model = Adversario
    paginate_by = 9
    queryset = Adversario.objects.order_by('nome')
    context_object_name = 'adversarios'