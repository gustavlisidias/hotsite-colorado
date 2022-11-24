from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#from django.conf.urls import url
from django.urls import re_path as url 
from django.conf.urls.static import static
from django.views.static import serve 
from django.contrib.auth import views as auth_views
from main.views import (
    IndexView, 
    SuporteView,
    ColoradoShowView,
    
    MaquinasView,    
    ServicosView,
    PecasView,
    ImplementosView,
    AgriculturaView,
    ConsorcioView,
    SegurosView,
    
    AcessoriosView,
    BrinquedosView,
    UtensiliosView,
    
    ContatoCampanhaView,
    ContatoCollectionView
)

urlpatterns = [
    #URLs estáticas
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    #URLs iniciais
    path('admin', admin.site.urls),
    path('', IndexView, name="home"),
    path('suporte', SuporteView, name="suporte"),
    path('coloradoshow', ColoradoShowView, name="coloradoshow"),
    
    #URLs das Campanhas
    path('campanhas/maquinas-agricolas', MaquinasView, name="maquinas"),
    path('campanhas/servicos', ServicosView, name="servicos"),
    path('campanhas/pecas-e-acessorios', PecasView, name="pecas"),
    path('campanhas/implementos-multimarcas', ImplementosView, name="implementos"),
    path('campanhas/agricultura-de-precisao', AgriculturaView, name="agricultura"),
    path('campanhas/consorcio-nacional-john-deere', ConsorcioView, name="consorcio"),
    path('campanhas/seguros', SegurosView, name="seguro"),
    
    #URLs das Collections
    path('collections/roupas-e-acessorios', AcessoriosView, name="acessorios"),
    path('collections/miniaturas-e-brinquedos', BrinquedosView, name="brinquedos"),
    path('collections/utensilios', UtensiliosView, name="utensilios"),
    
    
    #URLs dos Leads
    path('campanhas/cadastrar-contato/<id_campanha>', ContatoCampanhaView, name="lead_campanha"),
    path('collections/cadastrar-contato/<id_collection>', ContatoCollectionView, name="lead_collection"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Configuração dos campos Admin
admin.site.site_header = 'Hotsite Colorado Máquinas'
admin.site.site_title = 'Hotsite Colorado Máquinas'
admin.site.index_title = 'Administração'
admin.empty_value_display = '**Empty**'