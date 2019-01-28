from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from jogo.forms import ContatoForm


class ContatoView(View):

    template = 'jogo/contato.html'

    def get(self, request):
        form = ContatoForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome_time = form.cleaned_data['nome_time']
            nome_contato = form.cleaned_data['nome_contato']
            whats = form.cleaned_data['whats']
            email = form.cleaned_data['email']

            corpo = f'Nome do Time: {nome_time}\n' \
                    f'Nome Contato: {nome_contato}\n' \
                    f'WhatsApp: {whats}\n' \
                    f'E-mail: {email}'

            send_mail(
                'Contato Realmatismo FC',  # Assunto
                corpo,
                'diegodenzer.devops@gmail.com',
                ['realmatismo.cwb@gmail.com', 'marlosgiovanni@hotmail.com']
            )

            msg = 'Cadastro Realizado com sucesso!!!'

            return render(request, self.template, {'form': ContatoForm(), 'msg': msg})
        else:
            return render(request, self.template, {'form': form})
