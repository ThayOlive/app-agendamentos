from django.shortcuts import render, redirect
from .forms import DadosForm
from django.contrib import messages

def agendamento(request):
    
    if request.method == 'POST':
        form = DadosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Treinamento agendado com sucesso!")
            return render(request, 'agendamento.html')
        else:
            messages.error(request,"Falha ao agendar, verifique os dados e tente novamente!")
            form=DadosForm()
    else:
        form = DadosForm()
    context= {
        'form': form
    }
    return render(request, 'agendamento.html', context)

