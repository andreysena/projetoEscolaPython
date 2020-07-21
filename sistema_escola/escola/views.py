from django.shortcuts import render, redirect

# Create your views here.
from .models import Funcionario, Materia, Professor, Coordenador, Turma, Aluno
from .form import FuncionairoForm, MateriaForm, ProfessorForm, CoordenadorForm, TurmaForm, AlunoForm


########################### FUNÇÕES PARA REALIZAR O CRUD DE FUNCIONÁRIO ###########################


def listafunc(request):
    data = {}
    data["Funcionario"] = Professor.objects.all()
    return render(request, "Funcionario/listaFuncionario.html", data)


def cadfunc(request):
    data = {}
    form = FuncionairoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemFunc")

    data['form'] = form
    return render(request, "Funcionario/cadFuncionario.html", data)


def altfunc(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionairoForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('url_listagemFunc')

    data['form'] = form
    return render(request, "Funcionario/cadFuncionario.html", data)


def delfunc(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('url_listagemFunc')


########################### FUNÇÕES PARA REALIZAR O CRUD DE MATÉRIA ###########################


def listamat(request):
    data = {}
    data["Materia"] = Materia.objects.all()
    return render(request, "Materia/listaMateria.html", data)


def cadmat(request):
    data = {}
    form = MateriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemMat")

    data['form'] = form
    return render(request, "Materia/cadMateria.html", data)


def altmat(request, pk):
    data = {}
    materia = Materia.objects.get(pk=pk)
    form = MateriaForm(request.POST or None, instance=materia)

    if form.is_valid():
        form.save()
        return redirect('url_listagemMat')

    data['form'] = form
    return render(request, "Materia/cadMateria.html", data)


def delfunc(request, pk):
    materia = Funcionario.objects.get(pk=pk)
    materia.delete()
    return redirect('url_listagemMat')



########################### FUNÇÕES PARA REALIZAR O CRUD DE PROFESSOR ###########################


def listaprof(request):
    data = {}
    data["Professor"] = Professor.objects.all()
    return render(request, "Professor/listaProfessor.html", data)


def cadprof(request):
    data = {}
    form = ProfessorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemProf")

    data['form'] = form
    return render(request, "Professor/cadProfessor.html", data)


def altprof(request, pk):
    data = {}
    professor = Professor.objects.get(pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('url_listagemProf')

    data['form'] = form
    return render(request, "Professor/cadProfessor.html", data)


def delprof(request, pk):
    professor = Professor.objects.get(pk=pk)
    professor.delete()
    return redirect('url_listagemProf')


########################### FUNÇÕES PARA REALIZAR O CRUD DE COORDENADOR ###########################


def listacoord(request):
    data = {}
    data["Coordenador"] = Coordenador.objects.all()
    return render(request, "Coordenador/listaCoordenador.html", data)


def cadcoord(request):
    data = {}
    form = CoordenadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemCoord")

    data['form'] = form
    return render(request, "Coordenador/cadCoordenador.html", data)


def altcoord(request, pk):
    data = {}
    coordenador = Coordenador.objects.get(pk=pk)
    form = CoordenadorForm(request.POST or None, instance=coordenador)

    if form.is_valid():
        form.save()
        return redirect('url_listagemCoord')

    data['form'] = form
    return render(request, "Coordenador/cadCoordenador.html", data)


def delcoord(request, pk):
    coordenador = Coordenador.objects.get(pk=pk)
    coordenador.delete()
    return redirect('url_listagemCoord')


########################### FUNÇÕES PARA REALIZAR O CRUD DE TURMA ###########################


def listaturma(request):
    data = {}
    data["Turma"] = Turma.objects.all()
    return render(request, "Turma/listaTurma.html", data)


def cadturma(request):
    data = {}
    form = TurmaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemTurma")

    data['form'] = form
    return render(request, "Turma/cadTurma.html", data)


def altturma(request, pk):
    data = {}
    turma = Turma.objects.get(pk=pk)
    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('url_listagemTurma')

    data['form'] = form
    return render(request, "Turma/cadTurma.html", data)


def delturma(request, pk):
    turma = Turma.objects.get(pk=pk)
    turma.delete()
    return redirect('url_listagemTurma')


########################### FUNÇÕES PARA REALIZAR O CRUD DE TURMA ###########################


def listaturma(request):
    data = {}
    data["Turma"] = Turma.objects.all()
    return render(request, "Turma/listaTurma.html", data)


def cadturma(request):
    data = {}
    form = TurmaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemTurma")

    data['form'] = form
    return render(request, "Turma/cadTurma.html", data)


def altturma(request, pk):
    data = {}
    turma = Turma.objects.get(pk=pk)
    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('url_listagemTurma')

    data['form'] = form
    return render(request, "Turma/cadTurma.html", data)


def delturma(request, pk):
    turma = Turma.objects.get(pk=pk)
    turma.delete()
    return redirect('url_listagemTurma')


########################### FUNÇÕES PARA REALIZAR O CRUD DE ALUNO ###########################


def listaaluno(request):
    data = {}
    data["Aluno"] = Aluno.objects.all()
    return render(request, "Aluno/listaAluno.html", data)


def cadaluno(request):
    data = {}
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagemAluno")

    data['form'] = form
    return render(request, "Aluno/cadAluno.html", data)


def altaluno(request, pk):
    data = {}
    aluno = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=Aluno)

    if form.is_valid():
        form.save()
        return redirect('url_listagemAluno')

    data['form'] = form
    return render(request, "Aluno/cadAluno.html", data)


def delaluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('url_listagemAluno')



