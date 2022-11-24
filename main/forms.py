from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory, BaseFormSet, formset_factory
from main.models import (
    Campanha,
    Collection,
    ContatoCampanha,
    ContatoCollection,
    Midia,
    Keyword
)


#Form para o contate-nos na home, sem cadastro em banco de dados, apenas envio de email
class FormContato(forms.Form):
    nome        = forms.CharField(required=True)
    email       = forms.EmailField(required=True)
    assunto     = forms.CharField(required=True)
    mensagem    = forms.CharField(widget=forms.Textarea, required=True)
    

#form do detalhamento de vagas
class FormContatoCampanha(forms.ModelForm):
    class Meta:
        model = ContatoCampanha
        fields = '__all__'   
        exclude = ['campanha', 'data_contato']

    
#form do detalhamento de vagas
class FormContatoCollection(forms.ModelForm):
    class Meta:
        model = ContatoCollection
        fields = '__all__'
        exclude = ['collection', 'data_contato']