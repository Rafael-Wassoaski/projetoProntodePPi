from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode
from .forms import QuizForm, PerguntasForm
from .models import Quiz, Pergunta
from django.forms.formsets import formset_factory
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from django.contrib import messages

	# Create your views here.

def quizList(request):
	quizs = Quiz.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

	return render(request, 'quiz/HTML/quizList.html', {'quizs':quizs})

def fazerQuiz(request, pkQuiz):
	quiz = Quiz.objects.get(pk = pkQuiz)
	perguntas = Pergunta.objects.filter(quiz = quiz)
	# respostasFormSet = formset_factory(RespostaForm, extra=quiz.numPerguntas)
	# formSet = respostasFormSet()
	
	if request.method == "POST":
		pontos = 0


		for pergunta in perguntas:
			resp = request.POST.get(str(pergunta.pergunta), '')
			respCorreta = pergunta.resposta
			if respCorreta == resp:
				pontos = pontos + 1
											
		messages.info(request, 'Você fez: {} pontos'.format(pontos) , extra_tags='alert')
		return redirect('quiz:quizList')


	return render(request, 'quiz/HTML/fazerQuiz.html', {'quiz':quiz,'perguntas':perguntas})


def mostrarPontos(request):
	pontos = request.GET.get('pontos')

	return render(request,'quiz/HTML/mostrarPontos.html', {'pontos':pontos})

@login_required
def CreateQuiz(request):
	quizForm = QuizForm()
	if request.method == "POST":
		quiz = QuizForm(request.POST)

		if quiz.is_valid():
			quiz = quiz.save(commit = False)
			quiz.author = request.user
			quiz.create_date = timezone.now()
			quiz.save()

			urlBase = reverse('quiz:criarPerguntas')
			quizPk = urlencode({'quiz':quiz.pk, 'quantidade':quiz.numPerguntas})

			url = '{}?{}'.format(urlBase, quizPk)
			return redirect(url)

	return render(request, 'quiz/HTML/quiz_form.html', {'quizForm':quizForm,})

@login_required
def CreatePerguntas(request):
	pkQuiz = request.GET.get('quiz')
	quantidade = int(request.GET.get('quantidade'))
	
	perguntaForm = PerguntasForm()
	
	if request.method == "POST":
	    pergunta = PerguntasForm(request.POST)

	    if pergunta.is_valid():
	    	pergunta = pergunta.save(commit = False)
	    	pergunta.quiz = Quiz.objects.get(pk = pkQuiz)
	    	pergunta.save()
	

	    	if quantidade - 1 > 0:
		    	urlBase = reverse('quiz:criarPerguntas')
		    	urlParameters = urlencode({'quiz': pkQuiz, 'quantidade': quantidade - 1})
		    	url = '{}?{}'.format(urlBase, urlParameters)
		    	return redirect(url)

	    	return redirect('quiz:quizList')

	return render(request, 'quiz/HTML/createPerguntas.html', {'pergunta': perguntaForm,})






