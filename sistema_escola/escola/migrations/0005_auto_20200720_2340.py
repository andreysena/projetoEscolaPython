# Generated by Django 3.0.8 on 2020-07-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_auto_20200720_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='numero_cracha',
        ),
        migrations.AddField(
            model_name='professor',
            name='numero_aulas',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
