from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from unidecode import unidecode
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField


#Grupos de classes
GRUPO = [
    ('Campanha', 'Campanha'),
    ('Collection', 'Collection'),
]


#Função para source no cadastro de imagem dos grupos
def ImagemClasse(request, filename):
    src = 'classes/{filename}'.format(filename=unidecode(filename))
    return src


#Função para source no cadastro de imagem da campanha
def ImagemCampanha(request, filename):
    src = 'campanhas/{filename}'.format(filename=unidecode(filename))
    return src


#Função para source no cadastro de imagem da collection
def ImagemCollection(request, filename):
    src = 'collections/{filename}'.format(filename=unidecode(filename))
    return src


#Função para source no cadastro de imagem dos grupos
def ImagemConecta(request, filename):
    src = 'conecta/{filename}'.format(filename=unidecode(filename))
    return src


#Função para source no cadastro de imagem da colorado show
def ImagemColorado(request, filename):
    src = 'coloradoshow/{filename}'.format(filename=unidecode(filename))
    return src


# main_classes (Classes - Grupos Cadastrais)
class Classes(models.Model):
    nome                    = models.CharField(max_length=128, verbose_name="Nome")
    descricao               = RichTextField(null=True, blank=True, verbose_name="Descrição")
    url                     = models.CharField(max_length=128, null=True, blank=True, verbose_name="URL (Não alterar!)")
    grupo                   = models.CharField(max_length=64, choices=GRUPO, verbose_name="Grupo")
    status                  = models.BooleanField(default=True, verbose_name="Status")
    imagem                  = models.ImageField(upload_to=ImagemClasse, verbose_name="Imagem (450x500)", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "5.0 - Classes" 


# main_campanha (Campanhas)
class Campanha(models.Model):
    campanha                 = models.CharField(max_length=128, verbose_name="Campanha")
    grupo                    = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Classe")
    descricao                = RichTextField(null=True, blank=True, verbose_name="Descrição")
    informacoes              = RichTextField(null=True, blank=True, verbose_name="Informações Adicionais")
    local                    = models.CharField(max_length=128, null=True, blank=True, verbose_name="Local")
    contato1                 = models.CharField(max_length=128, null=True, blank=True, verbose_name="Celular")
    contato2                 = models.CharField(max_length=128, null=True, blank=True, verbose_name="Telefone")
    keyword                  = models.CharField(max_length=128, verbose_name="SEO")
    status                   = models.BooleanField(default=True, verbose_name="Status")
    imagem                   = models.ImageField(upload_to=ImagemCampanha, verbose_name="Imagem (450x500)", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return self.campanha
    
    class Meta:
        verbose_name = "Campanha"
        verbose_name_plural = "5.1 - Campanhas" 


# main_collection (Collections)
class Collection(models.Model):
    collection               = models.CharField(max_length=128, verbose_name="Collection")
    grupo                    = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Classe")
    descricao                = RichTextField(null=True, blank=True, verbose_name="Descrição")
    informacoes              = RichTextField(null=True, blank=True, verbose_name="Informações Adicionais")
    local                    = models.CharField(max_length=128, null=True, blank=True, verbose_name="Local")
    contato1                 = models.CharField(max_length=128, null=True, blank=True, verbose_name="Celular")
    contato2                 = models.CharField(max_length=128, null=True, blank=True, verbose_name="Telefone")
    keyword                  = models.CharField(max_length=128, verbose_name="SEO")
    status                   = models.BooleanField(default=True, verbose_name="Status")
    imagem                   = models.ImageField(upload_to=ImagemCollection, verbose_name="Imagem (450x500 ou Superior)", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.collection
    
    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "5.1 - Collections" 
        

# main_contatocampanha (LEAD das Campanhas)
class ContatoCampanha(models.Model):
    campanha                 = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, blank=True)
    nome                     = models.CharField(max_length=64, verbose_name="Nome Contato")
    email                    = models.EmailField(max_length=64, verbose_name="Email Contato")
    assunto                  = models.CharField(max_length=128, verbose_name="Assunto Contato")
    mensagem                 = models.TextField(max_length=512, verbose_name="Mensagem Contato")
    numero                   = models.CharField(max_length=32, null=True, blank=True, verbose_name="Numero Contato")
    data_contato             = models.DateTimeField(auto_now_add=True, verbose_name="Data Contato")
    
    def __str__(self):
        return self.nome + ' - ' + str(self.campanha)
    
    class Meta:
        verbose_name = "Lead Campanha"
        verbose_name_plural = "5.2 - Lead Campanhas" 
        

# main_contatocollection (LEAD das Collections)
class ContatoCollection(models.Model):
    collection               = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True, blank=True)
    nome                     = models.CharField(max_length=64, verbose_name="Nome Contato")
    email                    = models.EmailField(max_length=64, verbose_name="Email Contato")
    assunto                  = models.CharField(max_length=128, verbose_name="Assunto Contato")
    mensagem                 = models.TextField(max_length=512, verbose_name="Mensagem Contato")
    numero                   = models.CharField(max_length=32, null=True, blank=True, verbose_name="Numero Contato")
    data_contato             = models.DateTimeField(auto_now_add=True, verbose_name="Data Contato")
    
    def __str__(self):
        return self.nome + ' - ' + str(self.collection)
    
    class Meta:
        verbose_name = "Lead Collection"
        verbose_name_plural = "5.2 - Lead Collections" 
        
        
# main_keyword (SEO)
class Keyword(models.Model):
    keyword                  = models.CharField(max_length=128, verbose_name="SEO")
    descricao                = models.CharField(max_length=128, null=True, blank=True, verbose_name="Descrição SEO")
    status                   = models.BooleanField(default=True, verbose_name="Status")

    def __str__(self):
        return self.keyword
    
    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "1.0 - SEO" 
        

# main_conecta (App Conecta)
class Conecta(models.Model):
    publicacao               = models.CharField(max_length=128, verbose_name="Publicação App Conecta")
    descricao                = RichTextField(null=True, blank=True, verbose_name="Descrição")
    status                   = models.BooleanField(default=False, verbose_name="Status")
    imagem                   = models.ImageField(upload_to=ImagemConecta, verbose_name="Imagem (420x520)", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.publicacao
    
    class Meta:
        verbose_name = "App Conecta"
        verbose_name_plural = "2.0 - App Conecta" 


# main_coloradoshow (Colorado Show)
class ColoradoShow(models.Model):
    publicacao               = models.CharField(max_length=128, verbose_name="Publicação Colorado Show")
    descricao                = RichTextField(null=True, blank=True, verbose_name="Descrição")
    status                   = models.BooleanField(default=False, verbose_name="Status")
    imagem                   = models.ImageField(upload_to=ImagemColorado, verbose_name="Imagem (420x520)", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.publicacao
    
    class Meta:
        verbose_name = "Colorado Show"
        verbose_name_plural = "2.0 - Colorado Show" 
        

# main_suporte (Cadastros de Suporte)
class Suporte(models.Model):
    suporte               = models.CharField(max_length=128, verbose_name="Suporte")
    telefone              = models.CharField(max_length=128, null=True, blank=True, verbose_name="Telefone")
    celular               = models.CharField(max_length=128, null=True, blank=True, verbose_name="Celular")
    email                 = models.EmailField(max_length=64, null=True, blank=True, verbose_name="Email")

    def __str__(self):
        return self.suporte
    
    class Meta:
        verbose_name = "Canal de Suporte"
        verbose_name_plural = "3.0 - Canais de Suporte" 
        
        
# main_midia (Videos do YouTube)
class Midia(models.Model):
    midia                    = models.CharField(max_length=128, verbose_name="Nome da Mídia")
    url                      = models.URLField(max_length=512, verbose_name="URL da Mídia")
    descricao                = RichTextField(max_length=128, null=True, blank=True, verbose_name="Descrição da Mídia")

    def __str__(self):
        return self.midia
    
    class Meta:
        verbose_name = "Webserie"
        verbose_name_plural = "4.0 - Webseries" 