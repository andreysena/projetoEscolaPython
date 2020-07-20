from django.contrib import admin
from .models import Professor, Materia, Aluno, Funcionario, Turma, Coordenador

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Coordenador)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Materia)


