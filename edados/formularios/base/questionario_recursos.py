# from django import forms

# class questionario_recursos_especializados(forms.Form):
#     IN_SEM_RECURSO = forms.BooleanField(label='Sem recurso', required=False)
#     IN_BRAILLE = forms.BooleanField(label='Braille', required=False)
#     IN_AMPLIADA_24 = forms.BooleanField(label='Ampliada 24', required=False)
#     IN_AMPLIADA_18 = forms.BooleanField(label='Ampliada 18', required=False)
#     IN_LEDOR = forms.BooleanField(label='Ledor', required=False)
#     IN_ACESSO = forms.BooleanField(label='Acesso', required=False)
#     IN_TRANSCRICAO = forms.BooleanField(label='Transcrição', required=False)
#     IN_LIBRAS = forms.BooleanField(label='Libras', required=False)
#     IN_TEMPO_ADICIONAL = forms.BooleanField(label='Tempo adicional', required=False)

#     def clean(self):
#         cleaned_data = super().clean()
#         for key, value in cleaned_data.items():
#             if value is None:
#                 cleaned_data[key] = False
#         return cleaned_data


from random import choices
from django import forms

def questionario_recursos_especializados(Form):

    recursos_especializados = (
        ('nenhum', 'Nenhum recurso'),
        ('todos', 'Todos os recursos'),
        ('IN_SEM_RECURSO', 'IN_SEM_RECURSO'),
        ('IN_BRAILLE', 'IN_BRAILLE'),
        ('IN_AMPLIADA_24', 'IN_AMPLIADA_24'),
        ('IN_AMPLIADA_18', 'IN_AMPLIADA_18'),
        ('IN_LEDOR', 'IN_LEDOR'),
        ('IN_ACESSO', 'IN_ACESSO'),
        ('IN_TRANSCRICAO', 'IN_TRANSCRICAO'),
        ('IN_LIBRAS', 'IN_LIBRAS'),
        ('IN_TEMPO_ADICIONAL', 'IN_TEMPO_ADICIONAL'),
    )

    recursos_especializados = forms.ChoiceField(choices=recursos_especializados, label='Recurso utilizado:', required=False)

    return recursos_especializados
