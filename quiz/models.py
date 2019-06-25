from django.db import models
from django.utils import timezone
from django.conf import settings

	# Create your models here.


class Quiz(models.Model):
	    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	    titulo =  models.CharField(max_length = 50)
	    descricao = models.TextField()
	    CATEGORIA=(
	        ('AV', 'Aventura'),
	        ('PR', 'Personagem'),
	        ('IT', 'Item'),
	        ('FC', 'Ficha'),
	        ('TM', 'Tema Livre'),
	        )
	    categoria = models.CharField(max_length=2, choices=CATEGORIA, default='AV')
	    numPerguntas = models.IntegerField()
	    create_date = models.DateTimeField(blank = True, null = True)

	    def publish(self):
	    	self.published_date = timezone.now()
	    	self.save()

	    def __str__(self):
	    	return self.title

	    




class Pergunta(models.Model):
		quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
		pergunta = models.TextField()
		resposta = models.CharField(max_length = 200)
		dica = models.TextField(blank = True, default='Sem dica')		


		


# class Resposta(models.Model):
# 	pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE)
# 	resposta = models.CharField(max_length = 200)
	

