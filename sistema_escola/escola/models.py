from django.db import models

# Create your models here.

# CRIANDO A TABELA FUNCIONARIO
class Funcionario(models.Model):
    ID_Funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=45)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=45)
    rg = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    salario = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'funcionario'


    def __str__(self):
        return self.nome_funcionario


# CRIANDO A TABELA MATERIA
class Materia(models.Model):
    ID_Materia = models.AutoField(primary_key=True)
    nome_materia = models.CharField(max_length=45)

    class Meta:
        db_table = 'materia'


    def __str__(self):  # Permite exibir uma String como identificação
        return self.nome_materia


# CRIANDO A TABELA PROFESSOR
class Professor(models.Model):
    ID_Professor = models.AutoField(primary_key=True)
    numero_cracha = models.CharField(max_length=45)
    Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    class Meta:
        db_table = 'professor'


    def __str__(self):
        return self.Funcionario.nome_funcionario


# CRIANDO A TABELA COORDENADOR
class Coordenador(models.Model):
    ID_Coordenador = models.AutoField(primary_key=True)
    numero_cracha = models.CharField(max_length=45)
    FK_Func_Cood = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coordenador'


    def __str__(self):
        return self.FK_Func_Cood


# CRIANDO A TABELA TURMA
class Turma(models.Model):
    ID_Turma = models.AutoField(primary_key=True)
    letra_turma = models.CharField(max_length=45)
    FK_Coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
    FK_Prof_Turma = models.ManyToManyField(Professor)

    class Meta:
        db_table = 'turma'


    def __str__(self):
        return self.letra_turma


# CRIANDO A TABELA ALUNO
class Aluno(models.Model):
    ID_Aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=45)
    matricula = models.CharField(max_length=45)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=45)
    rg = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    FK_Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        db_table = 'aluno'


    def __str__(self):
        return self.nome_aluno