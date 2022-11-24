from django.contrib import admin, messages
from django.utils.translation import ngettext
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


#Admin action para habilitar status da model
@admin.action(description='Ativar %(verbose_name_plural)s selecionados')
def ativar(self, request, queryset):
        name = self.model._meta.verbose_name
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d %s foi ativado.',
            '%d %s foram ativados.',
            updated,
        ) % (updated, name), messages.SUCCESS)   
        

#Admin action para desabilitar status da model         
@admin.action(description='Desativar %(verbose_name_plural)s selecionados')
def desativar(self, request, queryset):
        name = self.model._meta.verbose_name
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d %s foi desativado.',
            '%d %s foram desativados.',
            updated,
        ) % (updated, name), messages.SUCCESS)


#Admin model das Campanhas    
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('campanha', 'grupo', 'descricao', 'keyword', 'status')
    search_fields = ('campanha', 'grupo', 'descricao', 'keyword')
    readonly_field = ('status')
    actions = [ativar, desativar]
admin.site.register(Campanha, CampanhaAdmin)


#Admin model das Collections  
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collection', 'grupo', 'descricao', 'keyword', 'status')
    search_fields = ('collection', 'grupo', 'descricao', 'keyword')
    readonly_field = ('status')
    actions = [ativar, desativar]
admin.site.register(Collection, CollectionAdmin)


#Admin model dos contatos das Campanhas
class ContatoCampanhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero', 'data_contato', 'campanha')
    search_fields = ('nome', 'email', 'numero', 'data_contato', 'campanha__campanha')
admin.site.register(ContatoCampanha, ContatoCampanhaAdmin)


#Admin model dos contatos das Collections 
class ContatoCollectionAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero', 'data_contato', 'collection')
    search_fields = ('nome', 'email', 'numero', 'data_contato', 'collection__collection')
admin.site.register(ContatoCollection, ContatoCollectionAdmin)


#Admin model dos videos do youtube  
admin.site.register(Midia)


#Admin model das Keywords (SEO)  
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'descricao', 'status')
    search_fields = ('keyword', 'descricao')
    readonly_field = ('status')
    actions = [ativar, desativar]
    
    # def save_model(self, request, obj, form, change):
        # obj.save()
        # seo = ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
        # f = open('media/SEO.txt', 'w')
        # f.write(seo)
        # f.close()  
    
    # def delete_model(self, request, obj):
        # obj.delete()
        # seo = ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
        # f = open('media/SEO.txt', 'w')
        # f.write(seo)
        # f.close()  
    
    # def delete_queryset(self, request, queryset):
        # queryset.delete()
        # seo = ', '.join([str(i) for i in Keyword.objects.filter(status=True)])
        # f = open('media/SEO.txt', 'w')
        # f.write(seo)
        # f.close()    
admin.site.register(Keyword, KeywordAdmin)


#Admin model dos cadastros de Classes
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo', 'status')
    search_fields = ('nome', 'grupo')
    readonly_field = ('status')
admin.site.register(Classes, ClassesAdmin)


#Admin model da configuração do App Conecta
class ConectaAdmin(admin.ModelAdmin):
    list_display = ('publicacao', 'descricao', 'status')
    search_fields = ('publicacao', 'descricao')
    readonly_field = ('status')
admin.site.register(Conecta, ConectaAdmin)

#Admin model da configuração do Colorado Show
class ColoradoShowAdmin(admin.ModelAdmin):
    list_display = ('publicacao', 'descricao', 'status')
    search_fields = ('publicacao', 'descricao')
    readonly_field = ('status')
admin.site.register(ColoradoShow, ColoradoShowAdmin)


#Admin model dos cadastros de Canais de Suporte
class SuporteAdmin(admin.ModelAdmin):
    list_display = ('suporte', 'telefone', 'celular', 'email')
    search_fields = ('suporte', 'telefone', 'celular', 'email')
admin.site.register(Suporte, SuporteAdmin)