# Generated by Django 4.2.1 on 2023-05-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.CharField(default=2, max_length=5),
            preserve_default=False,
        ),
    ]