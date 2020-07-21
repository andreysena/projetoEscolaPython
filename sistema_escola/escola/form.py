from django.forms import ModelForm

from .models import Professor


class ProfForm(ModelForm):

    class Meta:
        model = Professor
        fields = ['numero_aulas', 'Funcionario', 'Materia']
