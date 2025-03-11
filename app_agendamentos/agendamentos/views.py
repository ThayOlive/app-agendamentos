from django.shortcuts import render
from .forms import DadosForm
from django.contrib import messages

def agendamento(request):
    if request.method == 'POST':
        form = DadosForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success("Treinamento agendado com sucesso!")
        else:
            messages.error("Falha ao agendar, verifique os dados e tente novamente!")
    else:
        form = DadosForm()
    
    
    context= {
        'form': form
    }
    return render(request, 'agendamento.html', context)

