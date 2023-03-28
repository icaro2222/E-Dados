from random import choices
from django import forms


class VazioFormulario(forms.Form):

    choices_sexo = (('' ,''))

    sexo = forms.ChoiceField(choices=choices_sexo)