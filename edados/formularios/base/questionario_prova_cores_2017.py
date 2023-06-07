from random import choices
from django import forms


def questionario_prova(Form):

    choices_prova = (
        ('1-Dia, Prova de Ciências Humanas', (
                ('395', '395 - Azul'),
                ('396', '396 - Amarela'),
                ('397', '397 - Branca'),
                ('398', '398 - Rosa'),
                ('408', '408 - Laranja - Adaptada Ledor'),
                ('412', '412 - Verde - Videoprova - Libras'),
                ('435', '435 - Azul (Reaplicação)'),
                ('436', '436 - Amarelo (Reaplicação)'),
                ('437', '437 - Branco (Reaplicação)'),
                ('438', '438 - Rosa (Reaplicação)'),
                )
            ),
        ('1-Dia, Prova de Linguagens e Códigos', (
                ('399', '399 - Azul'),
                ('400', '400 - Amarela'),
                ('401', '401 - Rosa'),
                ('402', '402 - Branca'),
                ('409', '409 - Laranja - Adaptada Ledor'),
                ('413', '413 - Verde - Videoprova - Libras'),
                ('439', '439 - Azul (Reaplicação)'),
                ('440', '440 - Amarelo (Reaplicação)'),
                ('441', '441 - Branca (Reaplicação)'),
                ('442', '442 - Rosa (Reaplicação)'),
                )
            ),
        ('2-Dia, Prova de Ciências da Natureza',(
                ('391', '391 - Azul'),
                ('392', '392 - Amarela'),
                ('393', '393 - Cinza'),
                ('394', '394 - Rosa'),
                ('407', '407 - Laranja - Adaptada Ledor'),
                ('411', '411 - Verde - Videoprova - Libras'),
                ('431', '431 - Amarela (Reaplicação)'),
                ('432', '432 - Cinza (Reaplicação)'),
                ('433', '433 - Azul (Reaplicação)'),
                ('434', '434 - Rosa (Reaplicação)'),)
            ),
        ('2-Dia, Prova de Matemática', (
                ('403', '403 - Azul'),
                ('404', '404 - Amarela'),
                ('405', '405 - Rosa'),
                ('406', '406 - Cinza'),
                ('410', '410 - Laranja - Adaptada Ledor'),
                ('414', '414 - Verde - Videoprova - Libras'),
                ('443', '443 - Amarela (Reaplicação)'),
                ('444', '444 - Cinza (Reaplicação)'),
                ('445', '445 - Azul (Reaplicação)'),
                ('446', '446 - Rosa (Reaplicação'),
                )
            ),
        )

    prova_cores=forms.ChoiceField(
        label="Cor/Tipo da prova:", choices=choices_prova, required=False)
    return prova_cores

def questionario_prova_nenhuma(Form):

    choices_prova = (
        ('Nenhuma', (
            ("Nenhuma", "Nenhuma"),
                )
            ),
        ('1-Dia, Prova de Ciências Humanas', (
                ('395', '395 - Azul'),
                ('396', '396 - Amarela'),
                ('397', '397 - Branca'),
                ('398', '398 - Rosa'),
                ('408', '408 - Laranja - Adaptada Ledor'),
                ('412', '412 - Verde - Videoprova - Libras'),
                ('435', '435 - Azul (Reaplicação)'),
                ('436', '436 - Amarelo (Reaplicação)'),
                ('437', '437 - Branco (Reaplicação)'),
                ('438', '438 - Rosa (Reaplicação)'),
                )
            ),
        ('1-Dia, Prova de Linguagens e Códigos', (
                ('399', '399 - Azul'),
                ('400', '400 - Amarela'),
                ('401', '401 - Rosa'),
                ('402', '402 - Branca'),
                ('409', '409 - Laranja - Adaptada Ledor'),
                ('413', '413 - Verde - Videoprova - Libras'),
                ('439', '439 - Azul (Reaplicação)'),
                ('440', '440 - Amarelo (Reaplicação)'),
                ('441', '441 - Branca (Reaplicação)'),
                ('442', '442 - Rosa (Reaplicação)'),
                )
            ),
        ('2-Dia, Prova de Ciências da Natureza',(
                ('391', '391 - Azul'),
                ('392', '392 - Amarela'),
                ('393', '393 - Cinza'),
                ('394', '394 - Rosa'),
                ('407', '407 - Laranja - Adaptada Ledor'),
                ('411', '411 - Verde - Videoprova - Libras'),
                ('431', '431 - Amarela (Reaplicação)'),
                ('432', '432 - Cinza (Reaplicação)'),
                ('433', '433 - Azul (Reaplicação)'),
                ('434', '434 - Rosa (Reaplicação)'),)
            ),
        ('2-Dia, Prova de Matemática', (
                ('403', '403 - Azul'),
                ('404', '404 - Amarela'),
                ('405', '405 - Rosa'),
                ('406', '406 - Cinza'),
                ('410', '410 - Laranja - Adaptada Ledor'),
                ('414', '414 - Verde - Videoprova - Libras'),
                ('443', '443 - Amarela (Reaplicação)'),
                ('444', '444 - Cinza (Reaplicação)'),
                ('445', '445 - Azul (Reaplicação)'),
                ('446', '446 - Rosa (Reaplicação'),
                )
            ),
        )

    prova_cores=forms.ChoiceField(
        label="Cor/Tipo da prova:", choices=choices_prova, required=False)
    return prova_cores

def questionario_questao(Form):

    choices_numero_da_questao = (
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
            ("13", "13"),
            ("14", "14"),
            ("15", "15"),
            ("16", "16"),
            ("17", "17"),
            ("18", "18"),
            ("19", "19"),
            ("20", "20"),
            ("21", "21"),
            ("22", "22"),
            ("23", "23"),
            ("24", "24"),
            ("25", "25"),
            ("26", "26"),
            ("27", "27"),
            ("28", "28"),
            ("29", "29"),
            ("30", "30"),
            ("31", "31"),
            ("32", "32"),
            ("33", "33"),
            ("34", "34"),
            ("35", "35"),
            ("36", "36"),
            ("37", "37"),
            ("38", "38"),
            ("39", "39"),
            ("40", "40"),
            ("41", "41"),
            ("42", "42"),
            ("43", "43"),
            ("44", "44"),
            ("45", "45"),)

    numero_da_questao = forms.ChoiceField(label='Numero da Questao:', choices=choices_numero_da_questao, required=False)
    return numero_da_questao

def questionario_questao_nenhuma(Form):

    choices_numero_da_questao = (
            ("Nenhuma", "Nenhuma"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
            ("13", "13"),
            ("14", "14"),
            ("15", "15"),
            ("16", "16"),
            ("17", "17"),
            ("18", "18"),
            ("19", "19"),
            ("20", "20"),
            ("21", "21"),
            ("22", "22"),
            ("23", "23"),
            ("24", "24"),
            ("25", "25"),
            ("26", "26"),
            ("27", "27"),
            ("28", "28"),
            ("29", "29"),
            ("30", "30"),
            ("31", "31"),
            ("32", "32"),
            ("33", "33"),
            ("34", "34"),
            ("35", "35"),
            ("36", "36"),
            ("37", "37"),
            ("38", "38"),
            ("39", "39"),
            ("40", "40"),
            ("41", "41"),
            ("42", "42"),
            ("43", "43"),
            ("44", "44"),
            ("45", "45"),)

    numero_da_questao = forms.ChoiceField(label='Numero da Questao:', choices=choices_numero_da_questao, required=False)
    return numero_da_questao

