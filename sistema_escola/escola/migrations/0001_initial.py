# Generated by Django 3.0.8 on 2020-07-18 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('ID_Coordenador', models.AutoField(primary_key=True, serialize=False)),
                ('numero_cracha', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'coordenador',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('ID_Funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.CharField(max_length=45)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=45)),
                ('rg', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=45)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('ID_Materia', models.AutoField(primary_key=True, serialize=False)),
                ('nome_materia', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'materia',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('ID_Professor', models.AutoField(primary_key=True, serialize=False)),
                ('numero_cracha', models.CharField(max_length=45)),
                ('FK_Func_Prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Funcionario')),
                ('FK_Materia', models.ManyToManyField(to='escola.Materia')),
            ],
            options={
                'db_table': 'professor',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('ID_Serie', models.AutoField(primary_key=True, serialize=False)),
                ('nome_serie', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'serie',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('ID_Turma', models.AutoField(primary_key=True, serialize=False)),
                ('letra_turma', models.CharField(max_length=45)),
                ('FK_Coordenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Coordenador')),
                ('FK_Prof_Turma', models.ManyToManyField(to='escola.Professor')),
                ('FK_Serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Serie')),
            ],
            options={
                'db_table': 'turma',
            },
        ),
        migrations.AddField(
            model_name='coordenador',
            name='FK_Func_Cood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Funcionario'),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('ID_Aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome_aluno', models.CharField(max_length=45)),
                ('matricula', models.CharField(max_length=45)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=45)),
                ('rg', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=45)),
                ('FK_Turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Turma')),
            ],
            options={
                'db_table': 'aluno',
            },
        ),
    ]
