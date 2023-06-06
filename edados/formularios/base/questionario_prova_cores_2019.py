from random import choices
from django import forms


def questionario_prova(Form):

    choices_prova = (
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
