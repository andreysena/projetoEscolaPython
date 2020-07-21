from django.forms import ModelForm

from .models import Funcionario, Professor, Coordenador, Materia, Turma, Aluno


class FuncionairoForm(ModelForm):

    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'dt_nasc', 'cpf', 'rg', 'telefone', 'salario']


class MateriaForm(ModelForm):

    class Meta:
        model = Materia
        fields = ["nome_materia"]


class ProfessorForm(ModelForm):

    class Meta:
        model = Professor
        fields = ['numero_aulas', 'Funcionario', 'Materia']


class CoordenadorForm(ModelForm):

    class Meta:
        model = Coordenador
        fields = ["Funcionario"]


class TurmaForm(ModelForm):

    class Meta:
        model = Turma
        fields = ['letra_turma', 'Coordenador', 'Professores']


class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome_aluno', 'matricula', 'dt_nasc', 'cpf', 'rg', 'telefone', 'Turma']