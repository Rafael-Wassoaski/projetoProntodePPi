from django import forms

from .models import Character, Post, RespostaPost, Aventura
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
# RespostaRespotaPost

class CharacterForm(forms.ModelForm):
    """docstring for CharacterForm."""
    class Meta:
        model = Character
        fields =   '__all__'
        exclude = ['author']
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Row(
                
                Column('name', css_class='form-group col-md-3 col-md-offset-3'),
            	Column('classe', css_class='form-group col-md-3 col-md-offset-3'),   
            	Column('raca', css_class='form-group col-md-3'),
            	Column('sexo', css_class='form-group col-md-3'),         
              	css_class='form-row'
            ),
             Row(
                
                Column('tamanho', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('idade', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('altura', css_class='form-group col-sm-3'),
                Column('peso', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),

              Row(
                
                Column('olhos', css_class='form-group col-md-3 col-md-offset-3'),
                Column('cabelo', css_class='form-group col-md-3 col-md-offset-3'),   
                Column('pele', css_class='form-group col-md-3'),
                Column('divindade', css_class='form-group col-md-3'),         
                css_class='form-row'
            ),

                Row(
                
               
                 
                Column('forca', css_class='form-group col-sm-3'),
                Column('constituicao', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),

                Row(
                    Column('idiomas', css_class='form-group col-md12 col-md-offset-12'),  
                    css_class='form-row'
             ),

                Row(
                
                Column('destreza', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('inteligencia', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('sabedoria', css_class='form-group col-sm-3'),
                Column('carisma', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),
                Row(
                
                Column('pontosDeVida', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('iniciativa', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('deslocamento', css_class='form-group col-sm-3'),
                Column('tolerancia', css_class='form-group col-sm-3'),          
                css_class='form-row'
            ),
                Row(
                
                Column('acrobacia', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('atletismo', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('blefe', css_class='form-group col-sm-3'),
                Column('diplomacia', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),
                Row(
                
                Column('exploracao', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('furtividade', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('historia', css_class='form-group col-sm-3'),
                Column('intimidacao', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),
                Row(
                
                Column('intuicao', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('ladinagem', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('manha', css_class='form-group col-sm-3'),
                Column('natureza', css_class='form-group col-sm-3'),         
                css_class='form-row'
            ),

                Row(
                
                Column('percepcao', css_class='form-group col-sm-3 col-sm-offset-3'),
                Column('religiao', css_class='form-group col-sm-3 col-sm-offset-3'),   
                Column('socorro', css_class='form-group col-sm-3'), 
                css_class='form-row'
            ),

                Row(
                
            
                Column('rosto', css_class='form-group col-md-3'),      
                Column('tendencia', css_class='form-group col-md-3 col-md-offset-3'),  
                css_class='form-row'
            ),


            
            
        )
        self.helper.add_input(Submit('submit', 'Criar', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))
        


# class PericiasForm(forms.ModelForm):
#     class Meta:
#         model = Pericias
#         fields =   '__all__'
#         exclude = ['character']

#         def __init__(self, *args, **kwargs):
# 	        super(CharacterForm, self).__init__(*args, **kwargs)
# 	        self.helper = FormHelper(self)
# 	        self.helper.form_method = 'post'
# 	        self.helper.layout = Layout(
# 	            Row(
	                
# 	                Column('name', css_class='form-group col-md-4'),
# 	            	Column('classe', css_class='form-group col-md-4'),            
# 	              	css_class='form-row'
# 	            ),

# 	            Row(
# 	                Column('acrobacia', css_class='form-group col-md-2'),
# 	                Column('atletismo', css_class='form-group col-md-2'),
# 	                Column('blefe', css_class='form-group col-md-2'),
# 	                Column('diplomacia', css_class='form-group col-md-2'),
# 	                Column('exploracao', css_class='form-group col-md-2'),
# 	                Column('furtividade', css_class='form-group col-md-4'),
# 	                Column('historia', css_class='form-group col-md-2'),
# 	                Column('intimidacao', css_class='form-group col-md-2'),
# 	                Column('intuicao', css_class='form-group col-md-2'),
# 	                Column('ladinagem', css_class='form-group col-md-2'),
# 	                Column('manha', css_class='form-group col-md-2'),
# 	                Column('natureza', css_class='form-group col-md-2'),
# 	                Column('percepcao', css_class='form-group col-md-2'),
# 	                Column('religiao', css_class='form-group col-md-2'),
# 	                Column('socorro', css_class='form-group col-md-2'),
# 	                Column('tolerancia', css_class='form-group col-md-2'),

# 	                css_class='form-row'
# 	                ),

	            
	            
# 	        )
# 	        self.helper.add_input(Submit('submit', 'Postar'))
#        		self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'categoria',)
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),

        # }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                
                Column('title', css_class='form-group col-md-3 col-md-offset-3 mx-auto'),
                Column('categoria', css_class='form-group col-md-3 col-md-offset-3 mx-auto'),
                
                css_class='form-row'
            ),

            Row(
                Column('text', css_class='form-group col-md-12'),
                css_class='form-row'
            ),

            
            
        )
        self.helper.add_input(Submit('submit', 'Postar', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))



class RespostaForm(forms.ModelForm):
    class Meta:
        model = RespostaPost
        fields = ('resposta', )


    def __init__(self, *args, **kwargs):
        super(RespostaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                
                Column('resposta', css_class='form-group col-md-4 col-md-offset-4 mx-auto'),
               
                
                css_class='form-row'
            ),


            
            
        )
        self.helper.add_input(Submit('submit', 'Responder', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))
  



class AventuraForm(forms.ModelForm):
    class Meta:
        model = Aventura
        fields = '__all__'
        exclude = ['author', 'create_date', 'visitas']

    def __init__(self, *args, **kwargs):
        super(AventuraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                
                Column('titulo', css_class='form-group col-md-8 col-md-offset-8 mx-auto'),
                    
                css_class='form-row'
            ),
             Row(
                Column('aventura', css_class='form-group col-md-8 col-md-offset-8 mx-auto'),
               
                css_class='form-row'
            ),

            Row(
                Column('genero', css_class='form-group col-md-3 col-md-offset-3 mx-auto'),
              	Column('numeroJogadores', css_class='form-group col-md-3 col-md-offset-3 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column('npcs', css_class='form-group col-md-4 col-md-offset-4 mx-auto'),
                Column('itens', css_class='form-group col-md-4 col-md-offset-4 mx-auto'),
              	
                css_class='form-row'
            ),


            
            
        )
        self.helper.add_input(Submit('submit', 'Criar', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))
 

class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-3 mx-auto'),
                Column('assunto', css_class='form-group col-md-3 mx-auto'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn-success'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger '))

