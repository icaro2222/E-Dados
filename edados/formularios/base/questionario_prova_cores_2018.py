from random import choices
from django import forms


def questionario_prova(Form):

    choices_prova = (
        ('1-Dia, Prova de Ciências Humanas', (
                ('451', '451 - Azul'),
                ('452', '452 - Amarela'),
                ('453', '453 - Branca'),
                ('454', '454 - Rosa'),
                ('464', '464 - Laranja - Adaptada Ledor'),
                ('468', '468 - Verde - Videoprova - Libras'),
                ('491', '491 - Azul (Reaplicação)'),
                ('492', '492 - Amarelo (Reaplicação)'),
                ('493', '493 - Branco (Reaplicação)'),
                ('494', '494 - Rosa (Reaplicação)'),
                )
            ),
        ('1-Dia, Prova de Linguagens e Códigos', (
                ('455', '455 - Azul'),
                ('456', '456 - Amarela'),
                ('457', '457 - Rosa'),
                ('458', '458 - Branca'),
                ('465', '465 - Laranja - Adaptada Ledor'),
                ('469', '469 - Verde - Videoprova - Libras'),
                ('495', '495 - Azul (Reaplicação)'),
                ('496', '496 - Amarelo (Reaplicação)'),
                ('497', '497 - Branca (Reaplicação)'),
                ('498', '498 - Rosa (Reaplicação)'),
                )
            ),
        ('2-Dia, Prova de Ciências da Natureza',(
                ('447', '447 - Azul'),
                ('448', '448 - Amarela'),
                ('449', '449 - Cinza'),
                ('450', '450 - Rosa'),
                ('463', '463 - Laranja - Adaptada Ledor'),
                ('467', '467 - Verde - Videoprova - Libras'),
                ('487', '487 - Amarela (Reaplicação)'),
                ('488', '488 - Cinza (Reaplicação)'),
                ('489', '489 - Azul (Reaplicação)'),
                ('490', '490 - Rosa (Reaplicação)'),)
            ),
        ('2-Dia, Prova de Matemática', (
                ('459', '459 - Azul'),
                ('460', '460 - Amarela'),
                ('461', '461 - Rosa'),
                ('462', '462 - Cinza'),
                ('466', '466 - Laranja - Adaptada Ledor'),
                ('470', '470 - Verde - Videoprova - Libras'),
                ('499', '499 - Amarela (Reaplicação)'),
                ('500', '500 - Cinza (Reaplicação)'),
                ('501', '501 - Azul (Reaplicação)'),
                ('502', '502 - Rosa (Reaplicação'),
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
                ('507', '507 - Azul'),
                ('508', '508 - Amarela'),
                ('509', '509 - Branca'),
                ('510', '510 - Rosa'),
                ('520', '520 - Laranja - Adaptada Ledor'),
                ('524', '524 - Verde - Videoprova - Libras'),
                ('547', '547 - Azul (Reaplicação)'),
                ('548', '548 - Amarelo (Reaplicação)'),
                ('549', '549 - Branco (Reaplicação)'),
                ('550', '550 - Rosa (Reaplicação)'),
                ('564', '564 - Laranja - Adaptada Ledor (Reaplicação)'),
                )
            ),
        ('1-Dia, Prova de Linguagens e Códigos', (
                ('511', '511 - Azul'),
                ('512', '512 - Amarela'),
                ('513', '513 - Rosa'),
                ('514', '514 - Branca'),
                ('521', '521 - Laranja - Adaptada Ledor'),
                ('525', '525 - Verde - Videoprova - Libras'),
                ('551', '551 - Azul (Reaplicação)'),
                ('552', '552 - Amarelo (Reaplicação)'),
                ('553', '553 - Branca (Reaplicação)'),
                ('554', '554 - Rosa (Reaplicação)'),
                ('565', '565 - Laranja - Adaptada Ledor (Reaplicação)'),
                )
            ),
        ('2-Dia, Prova de Ciências da Natureza',(
                ('503', '503 - Azul'),
                ('504', '504 - Amarela'),
                ('505', '505 - Cinza'),
                ('506', '506 - Rosa'),
                ('519', '519 - Laranja - Adaptada Ledor'),
                ('523', '523 - Verde - Videoprova - Libras'),
                ('543', '543 - Amarela (Reaplicação)'),
                ('544', '544 - Cinza (Reaplicação)'),
                ('545', '545 - Azul (Reaplicação)'),
                ('546', '546 - Rosa (Reaplicação)'),)
            ),
        ('2-Dia, Prova de Matemática', (
                ('515', '515 - Azul'),
                ('516', '516 - Amarela'),
                ('517', '517 - Rosa'),
                ('518', '518 - Cinza'),
                ('522', '522 - Laranja - Adaptada Ledor'),
                ('526', '526 - Verde - Videoprova - Libras'),
                ('555', '555 - Amarela (Reaplicação)'),
                ('556', '556 - Cinza (Reaplicação)'),
                ('557', '557 - Azul (Reaplicação)'),
                ('558', '558 - Rosa (Reaplicação'),
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
