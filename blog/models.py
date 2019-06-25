from django.db import models
from django.utils import timezone
from django.conf import settings

from django.core.validators import MinValueValidator
from django.contrib import messages

class Post(models.Model):
    """docstring for Post."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField( 'Título' ,max_length = 200)
    text = models.TextField('Postagem')
    create_date = models.DateTimeField(blank = True, null = True)
    CATEGORIA=(
        ('AV', 'Aventura'),
        ('PR', 'Personagem'),
        ('IT', 'Item'),
        ('FC', 'Ficha'),
        ('TM', 'Tema Livre'),
        )
    categoria = models.CharField('Categoria' ,max_length=2, choices=CATEGORIA, default='AV')
    image = models.ImageField('Capa' ,upload_to = 'images/', blank = True, default = None)
    create_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class RespostaPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    resposta = models.TextField('Resposta');
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    repostaMain = models.ForeignKey('self', on_delete = models.CASCADE, null=True, blank = True)
    respResp = models.BooleanField(default = False)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        

class Character(models.Model):
    """docstring for Character."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField('Nome',max_length = 50)
    CLASSES = (
        ('BA','BARBARO'),
        ('LA', 'LADINO'),
        ('CL', 'CLERIGO'),
        

        )
    classe = models.CharField('Classe',max_length = 25)
    tamanho = models.IntegerField('Tamanho',default = 0, blank = True, null = True)
    RACAS = (

        ('HUM','HUMANO'),   
        ('DRA','DRACONATOS'),  
        ('ELF','ELFOS'), 
        ('GNO','GNOMOS'),
        ('ANO','ANOES'),
        ('HAL','HALFLINGS'),
        ('ELA','ELADRIN'),

        )
    raca = models.CharField('Raça',max_length = 15, choices = RACAS, default = 'HUMANO')
    idade = models.IntegerField('Idade',default = 0)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField('Sexo',max_length = 1, choices = SEX)
    altura = models.FloatField('Altura',default = 0)
    peso = models.FloatField('Peso',default = 0)
    olhos = models.CharField('Olhos',max_length = 20)
    cabelo = models.CharField('Cabelo',max_length = 30)
    pele = models.CharField('Pele',max_length = 30)
    divindade = models.CharField('Divindade',max_length = 50, default='', blank = True, null=True)

    TENDENCIA = (
        ('LG', 'LAWFUL GOOD'),
        ('NG', 'NEUTRAL GOOD'),
        ('CG', 'CHAOTIC GOOD'),
        ('LN', 'LAWFUL NEUTRAL'),
        ('TN', 'TRUE NEUTRAL'),
        ('CN', 'CHAOTIC NEUTRAL'),
        ('LE', 'LAWFUL EVIL'),
        ('NE', 'NEUTRAL EVIL'),
        ('CE', 'CHAOTIC EVIL'),
        )
    tendencia = models.CharField('Tendência',max_length=2, choices = TENDENCIA, default='LG')
    idiomas = models.TextField('Idiomas',default='', null = True, blank = True)
    forca = models.IntegerField('Força',default = 0)
    constituicao = models.IntegerField('Constituição',default = 0)
    destreza = models.IntegerField('Destreza',default = 0)  
    inteligencia = models.IntegerField('Inteligência',default = 0)
    sabedoria = models.IntegerField('Sabedoria',default = 0)
    carisma = models.IntegerField('Carisma',default = 0)
    pontosDeVida = models.IntegerField('Pontos de Vida',default = 5)
    iniciativa = models.IntegerField('Iniciativa',default = 0)
    deslocamento = models.IntegerField('Deslocamento',default = 2)
    rosto = models.ImageField('Rosto',upload_to='images/', blank = True,default = None)
    acrobacia = models.IntegerField('Acrobacia',default = 0)
    atletismo = models.IntegerField('Atletismo',default = 0)
    blefe = models.IntegerField('Blefe',default = 0)
    diplomacia = models.IntegerField('Diplomacia',default = 0)
    exploracao = models.IntegerField('Exploração',default = 0)
    furtividade = models.IntegerField('Furtividade',default = 0)
    historia = models.IntegerField('Historia',default = 0)
    intimidacao = models.IntegerField('Intimidação',default = 0)
    intuicao = models.IntegerField('Intuição',default = 0)
    ladinagem = models.IntegerField('Ladinagem',default = 0)
    manha = models.IntegerField('Manha',default = 0)
    natureza = models.IntegerField('Naruteza',default = 0)
    percepcao = models.IntegerField('Percepção',default = 0)
    religiao = models.IntegerField('Religião',default = 0)
    socorro = models.IntegerField('Socorro',default = 0)
    tolerancia = models.IntegerField('Tolerância',default = 0)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


# class Pericias(models.Model):
#     character = models.IntegerField()
#     acrobacia = models.IntegerField(default = 0)
#     atletismo = models.IntegerField(default = 0)
#     blefe = models.IntegerField(default = 0)
#     diplomacia = models.IntegerField(default = 0)
#     exploracao = models.IntegerField(default = 0)
#     furtividade = models.IntegerField(default = 0)
#     historia = models.IntegerField(default = 0)
#     intimidacao = models.IntegerField(default = 0)
#     intuicao = models.IntegerField(default = 0)
#     ladinagem = models.IntegerField(default = 0)
#     manha = models.IntegerField(default = 0)
#     natureza = models.IntegerField(default = 0)
#     percepcao = models.IntegerField(default = 0)
#     religiao = models.IntegerField(default = 0)
#     socorro = models.IntegerField(default = 0)
#     tolerancia = models.IntegerField(default = 0)
   

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.name

class Aventura(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    aventura = models.TextField(default = "")
    create_date = models.DateTimeField(blank = True, null = True)
    likes = models.IntegerField(default = 0);
    deslikes = models.IntegerField(default = 0);
    GENERO = (
        ('TR','Terror'),
        ('MD', 'Medieval'),
        ('CY', 'Cyberpunk'),
        ('MO', 'Moderno')
        )
    genero = models.CharField(max_length = 2, choices = GENERO, default= 'TR' )
    itens = models.TextField()
    numeroJogadores = models.IntegerField(default = 2, validators=[MinValueValidator(1, message = None  )])
    npcs = models.TextField()


