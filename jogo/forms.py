from django import forms


class ContatoForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail', 'class': 'validate', 'maxlength':'60'}))

    whats = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'WhatsApp', 'class': 'validate', 'maxlength': '14'}))

    nome_time = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome do Time', 'class': 'validate', 'maxlength': '60'}))

    nome_contato = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome do Time', 'class': 'validate', 'maxlength': '60'}))