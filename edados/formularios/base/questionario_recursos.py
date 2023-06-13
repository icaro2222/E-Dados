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
        ('vazio', 'Todos inscritos do enem'),
        ('todos', 'Algum dos recursos'),
        ('IN_SEM_RECURSO', 'Nenhum recurso'),
        ('IN_BRAILLE', 'Prova em braille'),
        ('IN_AMPLIADA_24', 'Prova superampliada com fonte tamanho 24'),
        ('IN_AMPLIADA_18', 'Prova ampliada com fonte tamanho 18'),
        ('IN_LEDOR', 'Auxílio para leitura (ledor)'),
        ('IN_ACESSO', 'Sala de fácil acesso'),
        ('IN_TRANSCRICAO', 'Auxílio para transcrição'),
        ('IN_LIBRAS', 'Tradutor- Intérprete Libras'),
        ('IN_TEMPO_ADICIONAL', 'Tempo adiciona'),
        ('IN_LEITURA_LABIAL', 'Leitura labial'),
        ('IN_MESA_CADEIRA_RODAS', 'Mesa para cadeira de rodas'),   
        ("IN_MESA_CADEIRA_SEPARADAIN_APOIO_PERNA", "Apoio de perna e pé"),
        ("IN_GUIA_INTERPRETE", "Guia intérprete"),
        ("IN_COMPUTADOR", "Computador"),
        ("IN_CADEIRA_ESPECIAL", "Cadeira especial"),
        ("IN_CADEIRA_CANHOTO", "Cadeira para canhoto"),
        ("IN_CADEIRA_ACOLCHOADA", "Cadeira acolchoada"),
        ("IN_MOBILIARIO_OBESO", "Mobiliário adequado para obeso"),
        ("IN_LAMINA_OVERLAY", "Lâmina overlay"),
        ("IN_PROTETOR_AURICULAR", "Protetor auricular"),
        ("IN_MEDIDOR_GLICOSE", "Medidor de glicose e/ou aplicação de insulina"),
        ("IN_MAQUINA_BRAILE", "Máquina Braile e/ou Reglete e Punção"),
        ("IN_SOROBAN", "Soroban"),
        ("IN_MARCA_PASSO", "Marca-passo (impeditivo de uso de detector de metais)"),
        ("IN_SONDA", "Sonda com troca periódica"),
        ("IN_MEDICAMENTOS", "Medicamentos"),
        ("IN_SALA_INDIVIDUAL", "Sala especial individual"),
        ("IN_SALA_ESPECIAL", "Sala especial até 20 participantes"),
        ("IN_SALA_ACOMPANHANTE", "Sala reservada para acompanhantes"),
        ("IN_MOBILIARIO_ESPECIFICO", "Mobiliário específico"),
        ("IN_MATERIAL_ESPECIFICO", "Material específico"),
        ("IN_PROVA_DEITADO", "Prova deitado em maca ou mobiliário similar"),
        ("IN_NOME_SOCIAL", "Atendimento pelo Nome Social"),
    )









    recursos_especializados = forms.ChoiceField(choices=recursos_especializados, label='Recurso utilizado:', required=False)

    return recursos_especializados
