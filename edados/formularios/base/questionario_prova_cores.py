from random import choices
from django import forms

def questionario_prova(Form):

    choices_prova = (('503','Azul'),
                    ('504','Amarela'),
                    ('505','Cinza'),
                    ('506','Rosa'),
                    ('519','Laranja - Adaptada Ledor'),
                    ('523','Verde - Videoprova - Libras'),
                    ('543','Amarela (Reaplicação)'),
                    ('544','Cinza (Reaplicação)'),
                    ('545','Azul (Reaplicação)'),
                    ('546','Rosa (Reaplicação)')
                    )

    prova_cores = forms.ChoiceField(label='Prova:', choices=choices_prova)
    return prova_cores




















