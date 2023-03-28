from random import choices
from django import forms

def questionario_estado_civil(Form):

    choices_estado_civil = (('todos', 'TODOS'),
                    ('0', 'Não informado'),
                    ('1' ,'Solteiro(a)'),
                    ('2' ,'Casado(a)/Moram juntos'),
                    ('3' ,'Divorciado(a)/Desquitado(a)/Separado(a)'),
                    ('4' ,'Viúvo(a)'))

    estado_civil = forms.ChoiceField(label='Estado Civil:', choices=choices_estado_civil)
    return estado_civil