# Generated by Django 3.0.8 on 2020-07-21 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_auto_20200720_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordenador',
            old_name='FK_Func_Cood',
            new_name='Funcionario',
        ),
    ]