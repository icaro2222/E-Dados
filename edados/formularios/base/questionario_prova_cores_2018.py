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
