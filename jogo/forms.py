from django.forms import forms


class TemporadaForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'quantidade', 'class': 'form-control form-control-alternative'}))

    whats = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'quantidade', 'class': 'form-control form-control-alternative'}))

    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'quantidade', 'class': 'form-control form-control-alternative'}))