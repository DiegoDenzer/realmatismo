from django.forms import forms


class TemporadaForm(forms.Form):

    ano = forms.IntegerField(initial=1, widget=forms.TextInput(attrs={'placeholder': 'quantidade',
                                                                      'class': 'form-control form-control-alternative'}))