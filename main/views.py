from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
import datetime
from main.models import (
    Classes,
    Campanha,
    Collection,
    ColoradoShow,
    ContatoCampanha,
    ContatoCollection,
    Midia,
    Keyword,
    Conecta,
    Suporte
)
from main.forms import (
    FormContato,
    FormContatoCampanha,
    FormContatoCollection
)


#View da homepage. Videos e SEO dinamicos 
def IndexView(request):
    index = 'Loja'
    videos = Midia.objects.all()
    classes = Classes.objects.all()
    conecta = Conecta.objects.all()
    coloradoshow = ColoradoShow.objects.all()
    seo = ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    if request.method == 'GET':
        form = FormContato(request.GET)
        mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3720.9299389317357!2d-47.760067485065036!3d-21.155186285930004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94b9c757961063bb%3A0xae2e902a1484e00a!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20(Matriz%20-%20Ribeir%C3%A3o%20Preto)!5e0!3m2!1spt-BR!2sbr!4v1629721938686!5m2!1spt-BR!2sbr'
        endereco    = 'Rodovia Anhanguera KM 313 + 220 m, Ribeirão Preto, SP, 14079-000'
        query = request.GET.get('q')
        if query == 'Ribeirao preto':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3720.9299389317357!2d-47.760067485065036!3d-21.155186285930004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94b9c757961063bb%3A0xae2e902a1484e00a!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20(Matriz%20-%20Ribeir%C3%A3o%20Preto)!5e0!3m2!1spt-BR!2sbr!4v1629721938686!5m2!1spt-BR!2sbr'
            endereco    = 'Rodovia Anhanguera, KM 313 + 220 m, Marginal Sul Rodovia SP 330 14079-000 Tel: (16) 3968-8080'
        if query == 'Araraquara':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3704.851957808427!2d-48.210186384981654!3d-21.785989904314526!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94b8e5be263ffd65%3A0x95a6f7d4b0c4245d!2sColorado%20M%C3%A1quinas%20Agr%C3%ADcolas!5e0!3m2!1spt-BR!2sbr!4v1629723542344!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Alberto Benassi, 3070 - Araraquara, SP, 14804-300'
        if query == 'Barretos':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3735.4147319373246!2d-48.581245985006476!3d-20.57111416387685!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bb85217d4b48bf%3A0x444b2a75ca87e414!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20-%20Barretos!5e0!3m2!1spt-BR!2sbr!4v1629723799803!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Eng. Necker Carvalho de Camargo, 2380 - América, Barretos - SP, 14783-080'
        if query == 'Guaira':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3741.2149500236524!2d-48.31321618557155!3d-20.33273695620841!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bb09f2c98c0bfd%3A0xc1cc206a8a0640f8!2sColorado%20Com%C3%A9rcio%20de%20M%C3%A1quinas%20Agr%C3%ADcolas!5e0!3m2!1spt-BR!2sbr!4v1629725232309!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Dr. João Batista Santana, 1875, Guaíra - SP, 14790-000'
        if query == 'Ituverava':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3740.9971077711716!2d-47.7960265855713!3d-20.34173815649639!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ba5d22e6324d1f%3A0x7934e82b47a8730f!2sColorado%20M%C3%A1quinas!5e0!3m2!1spt-BR!2sbr!4v1629725205277!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Dr. Paulo Borges de Oliveira, 1086 - Jardim Cristina, Ituverava - SP, 14500-000'
        if query == 'Orlandia':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3731.8357719198198!2d-47.89574098556249!3d-20.7168924686077!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ba252e28469529%3A0xadcf55e4c09c2b68!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20-%20Orl%C3%A2ndia!5e0!3m2!1spt-BR!2sbr!4v1629725176134!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Marginal Esquerda, 725 - Jardim Ciranda, Orlândia - SP, 14620-000'
        if query == 'Bebedouro':
           mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3726.3360326058587!2d-48.4519113855573!3d-20.93901637588116!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bbe4235bb55c7d%3A0x4a6ed01daff46ef7!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20-%20Bebedouro!5e0!3m2!1spt-BR!2sbr!4v1629725150109!5m2!1spt-BR!2sbr'
           endereco    = 'Av. Elisio de Oliveira, 1000 - Pioneiro, Bebedouro - SP, 14711-318'
        if query == 'Monte Alto':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3718.2631623200336!2d-48.4824958855494!3d-21.26104818656135!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94b946ab1561c67b%3A0x2daef0d5df22e30b!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20-%20Monte%20Alto!5e0!3m2!1spt-BR!2sbr!4v1629725122568!5m2!1spt-BR!2sbr'
            endereco    = 'R. Marginal Ítalo Lanfredi, 101 - Jardim das Nações - Jardim Santana, Monte Alto - SP, 15910-000'
        if query == 'Franca':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3736.0059694061893!2d-47.43474948556652!3d-20.546936663093973!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ba081f3ac54783%3A0x26ada0d85653d2f2!2sColorado%20M%C3%A1quinas%20%7C%20John%20Deere%20-%20Franca!5e0!3m2!1spt-BR!2sbr!4v1629725093678!5m2!1spt-BR!2sbr'
            endereco    = 'Av. Wilson Sábio de Mello, 2261 - Res. Oswaldo Maciel, Franca - SP, 14406-052'
        if query == 'Itapolis':
            mapa        = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3709.687589475897!2d-48.830399985057575!3d-21.59811448569264!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bed1d9bc012697%3A0x82830fe8a8646032!2sColorado%20Com%C3%A9rcio%20de%20M%C3%A1quinas%20Agr%C3%ADcola!5e0!3m2!1spt-BR!2sbr!4v1629725063475!5m2!1spt-BR!2sbr'
            endereco    = 'R. Rio de Janeiro, 520 - FR, Itápolis - SP, 14900-000'
    
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            nome            = form.cleaned_data['nome']
            email           = form.cleaned_data['email']
            assunto         = form.cleaned_data['assunto']
            mensagem        = form.cleaned_data['mensagem']
            
            send_mail(assunto, mensagem, email, ['sac@coloradoagro.com.br'])
            messages.success(request, 'Mensagem enviada. Obrigado!', extra_tags='alert')
            return redirect("home")
        else:
            messages.error(request, 'Não foi possível enviar mensagem. Por favor tente novamente!', extra_tags='alert')
            return redirect("home")
        
    return render(request, "home.html", {
        'form': form, 
        'videos': videos,
        'classes': classes,
        'conecta': conecta,
        'coloradoshow': coloradoshow,
        'seo': seo,
        'index': index,
        'mapa': mapa,
        'endereco': endereco
        })


def SuporteView(request):
    index = 'Suporte & Atendimento'
    canais = Suporte.objects.all
    return render(request, "suporte.html", {'index': index, 'canais': canais})


def ColoradoShowView(request):
    return render(request, "coloradoshow.html", {})


################################ Views para as Campanhas ################################
def MaquinasView(request):
    index = 'Máquinas Agrícolas'
    queryset = Campanha.objects.filter(grupo=1, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=1)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
        
    return render(request, "campanhas/maquinas.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def ServicosView(request):
    index = 'Serviços'
    queryset = Campanha.objects.filter(grupo=2, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=2)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/servicos.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def PecasView(request):
    index = 'Peças & Acessórios'
    queryset = Campanha.objects.filter(grupo=11, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=3)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/pecas.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def ImplementosView(request):
    index = 'Implementos Multimarcas'
    queryset = Campanha.objects.filter(grupo=10, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=10)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/implementos.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def AgriculturaView(request):
    index = 'Agricultura de Precisão'
    queryset = Campanha.objects.filter(grupo=5, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=5)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/agricultura.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def ConsorcioView(request):
    index = 'Consórcio'
    queryset = Campanha.objects.filter(grupo=6, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=6)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/consorcio.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def SegurosView(request):
    index = 'Seguros'
    queryset = Campanha.objects.filter(grupo=12, status=True)
    seo = ', '.join([str(i) for i in Campanha.objects.values_list('keyword', flat=True).filter(status=True, grupo=6)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "campanhas/seguros.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


################################ Views para as Collections ################################
def AcessoriosView(request):
    index = 'Roupas & Acessórios'
    queryset = Collection.objects.filter(grupo=7, status=True)
    seo = ', '.join([str(i) for i in Collection.objects.values_list('keyword', flat=True).filter(status=True, grupo=7)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "collections/acessorios.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def BrinquedosView(request):
    index = 'Miniaturas & Brinquedos'
    queryset = Collection.objects.filter(grupo=9, status=True)
    seo = ', '.join([str(i) for i in Collection.objects.values_list('keyword', flat=True).filter(status=True, grupo=9)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "collections/brinquedos.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


def UtensiliosView(request):
    index = 'Utensílios'
    queryset = Collection.objects.filter(grupo=8, status=True)
    seo = ', '.join([str(i) for i in Collection.objects.values_list('keyword', flat=True).filter(status=True, grupo=8)]) + ', ' + ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
    
    return render(request, "collections/utensilios.html", {
        'queryset': queryset,
        'seo': seo,
        'index': index
    })


################################ Views para as Cadastros nos LEADS ################################
def ContatoCampanhaView(request, id_campanha):
    index = 'Cadastrar Contato'
    item = get_object_or_404(Campanha, pk=id_campanha)
    
    if request.method == 'GET':
        form = FormContatoCampanha(request.GET)
        request.session['form'] = request.META.get('HTTP_REFERER', '/')

    elif request.method == 'POST':
        form = FormContatoCampanha(request.POST)
        
        if form.is_valid():            
            nome            = form.cleaned_data['nome']
            email           = form.cleaned_data['email']
            assunto         = form.cleaned_data['assunto']
            mensagem        = form.cleaned_data['mensagem']
            numero          = form.cleaned_data['numero']
            data_contato    = datetime.datetime.now()
            
            ContatoCampanha(
                campanha        = item,  
                nome            = nome,
                email           = email,
                assunto         = assunto,
                mensagem        = mensagem,
                numero          = numero,
                data_contato    = data_contato
            ).save()
        
            send_mail(
                assunto, 
                'Lead Campanha: ' + item.campanha + '\n\n' + mensagem + '\n\nContato do ' + nome + ' em ' + str(data_contato.strftime("%d/%m/%Y")) + '\nNumero para contato: ' + numero, 
                email, 
                ['sac@coloradoagro.com.br']
            )
        
            messages.success(request, 'Contato cadastrado!')
            return HttpResponseRedirect(request.session['form'])
        
        else:
            messages.success(request, 'Ops! Algo deu errado. Tente novamente')
            return HttpResponseRedirect(request.session['form'])
    
    return render(request, "leads/lead_campanha.html", {'form': form, 'index': index})
    

def ContatoCollectionView(request, id_collection):
    index = 'Cadastrar Contato'
    item = get_object_or_404(Collection, pk=id_collection)
    
    if request.method == 'GET':
        form = FormContatoCollection(request.GET)
        request.session['form'] = request.META.get('HTTP_REFERER', '/')

    elif request.method == 'POST':
        form = FormContatoCollection(request.POST)
        
        if form.is_valid():            
            nome            = form.cleaned_data['nome']
            email           = form.cleaned_data['email']
            assunto         = form.cleaned_data['assunto']
            mensagem        = form.cleaned_data['mensagem']
            numero          = form.cleaned_data['numero']
            data_contato    = datetime.datetime.now()
            
            ContatoCollection(
                collection      = item,  
                nome            = nome,
                email           = email,
                assunto         = assunto,
                mensagem        = mensagem,
                numero          = numero,
                data_contato    = data_contato
            ).save()
        
            send_mail(
                assunto, 
                'Lead Collection: ' + item.collection + '\n\n' + mensagem + '\n\nContato do ' + nome + ' em ' + str(data_contato.strftime("%d/%m/%Y")) + '\nNumero para contato: ' + numero, 
                email, 
                ['sac@coloradoagro.com.br']
            )
            
            messages.success(request, 'Contato cadastrado!')
            return HttpResponseRedirect(request.session['form'])
        
        else:
            messages.success(request, 'Ops! Algo deu errado. Tente novamente')
            return HttpResponseRedirect(request.session['form'])
    
    return render(request, "leads/lead_collection.html", {'form': form, 'index': index})
