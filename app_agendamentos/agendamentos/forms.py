from django import forms
from .models import DadosGerais, Cliente, Docente, Treinamento

class DadosForm(forms.ModelForm):
    
    class Meta:
        model = DadosGerais
        fields = ("treinamento","docente", "proposta","empresa", "cliente", "status", "data_inicial", "data_final",
                  "dias_treinamento", "turno", "horas", "observacao")


#Formulário para cadastro de cliente
class FormCliente(forms.ModelForm):
        
        class Meta:
            model = Cliente
            fields = ("nome","regiao")
    
#Formulário para cadastro de docente
class FormDocente(forms.ModelForm):
     
    class Meta:
            model = Docente
            fields = ('nome',)
    

#Formulário para cadastro de treinamentos
class FormTreinamento(forms.ModelForm):
    
    class Meta:
        model = Treinamento
        fields = ("nome", "formacao", "modalidade")

