from random import choices
from django import forms


def questionario_de_deficiencia(Form):

    choices_deficiencia = (('ambos' ,'Todos'),    
                    ('IN_SEM_RECURSO', 'SEM RECURSO'),
                    ('IN_BRAILLE', 'Utilizou prova em Braille'),
                    ('IN_AMPLIADA_18', 'Prova Ampliada 18'),
                    ('IN_LEDOR', 'IN LEDOR'),
                    ('IN_ACESSO', 'IN ACESSO'),
                    ('IN_NOME_SOCIAL', 'Usou Nome Social'),
                    ('IN_TRANSCRICAO', 'IN_TRANSCRICAO'),
                    ('IN_LIBRAS', 'IN_LIBRAS'),
                    ('IN_TEMPO_ADICIONAL', 'IN_TEMPO_ADICIONAL'),
                    ('IN_LEITURA_LABIAL', 'IN_LEITURA_LABIAL'),
                    ('IN_MESA_CADEIRA_RODAS', 'IN_MESA_CADEIRA_RODAS'),
                    ('IN_MESA_CADEIRA_SEPARADA', 'IN_MESA_CADEIRA_SEPARADA'),
                    ('IN_APOIO_PERNA', 'IN_APOIO_PERNA'),
                    ('IN_GUIA_INTERPRETE', 'IN_GUIA_INTERPRETE'),
                    ('IN_COMPUTADOR', 'IN_COMPUTADOR'),
                    ('IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_ESPECIAL'),
                    ('IN_CADEIRA_CANHOTO', 'IN_CADEIRA_CANHOTO'),
                    ('IN_CADEIRA_ACOLCHOADA', 'IN_CADEIRA_ACOLCHOADA'),
                    ('IN_PROVA_DEITADO', 'IN_PROVA_DEITADO'),
                    ('IN_MOBILIARIO_OBESO', 'IN_MOBILIARIO_OBESO'),
                    ('IN_LAMINA_OVERLAY', 'IN_LAMINA_OVERLAY'),
                    ('IN_PROTETOR_AURICULAR', 'IN_PROTETOR_AURICULAR'),
                    ('IN_MEDIDOR_GLICOSE', 'IN_MEDIDOR_GLICOSE'),
                    ('IN_MAQUINA_BRAILE', 'IN_MAQUINA_BRAILE'),
                    ('IN_SOROBAN', 'IN_SOROBAN'),
                    ('IN_MARCA_PASSO', 'IN_MARCA_PASSO'),
                    ('IN_SONDA', 'IN_SONDA'),
                    ('IN_MEDICAMENTOS', 'IN_MEDICAMENTOS'),
                    ('IN_SALA_INDIVIDUAL', 'IN_SALA_INDIVIDUAL'),
                    ('IN_SALA_ESPECIAL', 'IN_SALA_ESPECIAL'),
                    ('IN_SALA_ACOMPANHANTE', 'IN_SALA_ACOMPANHANTE'),
                    ('IN_MOBILIARIO_ESPECIFICO', 'IN_MOBILIARIO_ESPECIFICO'),
                    ('IN_MATERIAL_ESPECIFICO', 'IN_MATERIAL_ESPECIFICO'))
    
    deficiencia = forms.ChoiceField(choices=choices_deficiencia)
    
    return deficiencia