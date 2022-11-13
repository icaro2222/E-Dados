from random import choices
from django import forms

def questionario_prova(Form):

    choices_prova = (
                ('503', 'Azul'),
                ('504', 'Amarela'),
                ('505', 'Cinza'),
                ('506', 'Rosa'),
                ('519', 'Laranja - Adaptada Ledor'),
                ('523', 'Verde - Videoprova - Libras'),
                ('543', 'Amarela (Reaplicação)'),
                ('544', 'Cinza (Reaplicação)'),
                ('545', 'Azul (Reaplicação)'),
                ('546', 'Rosa (Reaplicação)'),
                ('507', 'Azul'),
                ('508', 'Amarela'),
                ('509', 'Branca'),
                ('510', 'Rosa'),
                ('520', 'Laranja - Adaptada Ledor'),
                ('524', 'Verde - Videoprova - Libras'),
                ('547', 'Azul (Reaplicação)'),
                ('548', 'Amarelo (Reaplicação)'),
                ('549', 'Branco (Reaplicação)'),
                ('550', 'Rosa (Reaplicação)'),
                ('564', 'Laranja - Adaptada Ledor (Reaplicação)'),
                ('511', 'Azul'),
                ('512', 'Amarela'),
                ('513', 'Rosa'),
                ('514', 'Branca'),
                ('521', 'Laranja - Adaptada Ledor'),
                ('525', 'Verde - Videoprova - Libras'),
                ('551', 'Azul (Reaplicação)'),
                ('552', 'Amarelo (Reaplicação)'),
                ('553', 'Branca (Reaplicação)'),
                ('554', 'Rosa (Reaplicação)'),
                ('565', 'Laranja - Adaptada Ledor (Reaplicação)'),
                ('515', 'Azul'),
                ('516', 'Amarela'),
                ('517', 'Rosa'),
                ('518', 'Cinza'),
                ('522', 'Laranja - Adaptada Ledor'),
                ('526', 'Verde - Videoprova - Libras'),
                ('555', 'Amarela (Reaplicação)'),
                ('556', 'Cinza (Reaplicação)'),
                ('557', 'Azul (Reaplicação)'),
                ('558', 'Rosa (Reaplicação'))

    prova_cores = forms.ChoiceField(label='Prova:', choices=choices_prova)
    return prova_cores




















