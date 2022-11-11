from random import choices
from django import forms


class Formulario_filtro(forms.Form):

    choices_sexo = (('ambos' ,'Ambos'),    
                    ('F', 'Filtrar Apenas Femilino'),
                    ('M' ,'Filtrar Apenas Masculino'))

    sexo = forms.ChoiceField(choices=choices_sexo)