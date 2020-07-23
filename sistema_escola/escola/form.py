from django.forms import ModelForm

from .models import Funcionario, Professor, Coordenador, Materia, Turma, Aluno


class FuncionairoForm(ModelForm):

    class Meta:
        model = Funcionario
        fields = ['nome_do_funcionario', 'data_de_nascimento', 'cpf', 'rg', 'telefone', 'salario']


class MateriaForm(ModelForm):

    class Meta:
        model = Materia
        fields = ["nome_da_materia"]


class ProfessorForm(ModelForm):

    class Meta:
        model = Professor
        fields = ['numero_de_aulas', 'Funcionario', 'Materia']


class CoordenadorForm(ModelForm):

    class Meta:
        model = Coordenador
        fields = ["Funcionario"]


class TurmaForm(ModelForm):

    class Meta:
        model = Turma
        fields = ['letra_da_turma', 'Coordenador', 'Professores']


class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome_do_aluno', 'matricula', 'data_de_nascimento', 'cpf', 'rg', 'telefone', 'Turma']