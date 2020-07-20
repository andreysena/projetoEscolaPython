from django.shortcuts import render, redirect

# Create your views here.
from .models import Funcionario, Coordenador, Aluno, Professor, Materia, Turma
from .form import ProfForm


def listaprof(request):
    data = {}  # Cria um dicionário vazio.
    data["Professor"] = Professor.objects.all()  # objects é manager pronto
    # do Django que nos permitirá acessar os dados de determinado model
    return render(request, "Professor/listaProf.html", data)


def cadprof(request):
    data = {}
    form = ProfForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    data['form'] = form
    return render(request, "Professor/cadProfessor.html", data)
