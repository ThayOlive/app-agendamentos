from django import forms
from .models import DadosGerais

class DadosForm(forms.ModelForm):
    
    class Meta:
        model = DadosGerais
        fields = ("codigo_treinamento","treinamento","docente", "proposta","empresa", "cliente", "status", "data_inicial", "data_final",
                  "dias_treinamento", "turno", "horas", "observacao")


