from django import forms
from .models import Quiz, Pergunta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ('titulo', 'descricao', 'categoria','numPerguntas',)
	def __init__(self, *args, **kwargs):
		super(QuizForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.layout = Layout(
			Row(

			Column('titulo', css_class='form-group col-md-6 col-md-offset-6'),
			Column('categoria', css_class='form-group col-md-3'),    
			Column('numPerguntas', css_class='form-group col-md-3'),   
			css_class='form-row'
			),

			Row(
			Column('descricao', css_class='form-group col-md-8 col-md-offset-8 mx-auto'), 
			css_class='form-row'
			),
		)
		self.helper.add_input(Submit('submit', 'Criar', css_class='btn-success'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger'))



class PerguntasForm(forms.ModelForm):
	class Meta:
		model = Pergunta
		fields = ['pergunta', 'resposta','dica']
		exclude = ['quiz',]
	def __init__(self, *args, **kwargs):
		super(PerguntasForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.layout = Layout(
			Row(

			Column('pergunta', css_class='form-group col-md-6 col-md-offset-6 mx-auto'),
			
			
			css_class='form-row'
			),
			Row(

			Column('resposta', css_class='form-group col-md-6 col-md-offset-6 mx-auto'),
			
			css_class='form-row'
			),
			Row(

			Column('dica', css_class='form-group col-md-6 col-md-offset-6 mx-auto'),
			css_class='form-row'
			),

			
		)
		self.helper.add_input(Submit('submit', 'Criar Pergunta', css_class='btn-success'))
		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger'))

# class RespostaForm(forms.ModelForm):
# 	class Meta:
# 		model = Resposta
# 		fields = ['resposta']
# 	def __init__(self, *args, **kwargs):
# 		super(RespostaForm, self).__init__(*args, **kwargs)
# 		self.helper = FormHelper(self)
# 		self.helper.form_method = 'POST'
# 		self.helper.layout = Layout(
# 			Row(

# 			Column('resposta', css_class='form-group col-md-6 col-md-offset-6'),
			
# 			css_class='form-row'
# 			),

			
# 		)
# 		self.helper.add_input(Submit('submit', 'Postar'))
# 		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))








