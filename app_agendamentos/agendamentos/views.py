from django.shortcuts import render, redirect
from .forms import DadosForm, FormTreinamento, FormDocente, FormCliente
from django.contrib import messages

def agendamento(request):  
    if request.method == 'POST':
        form = DadosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Treinamento agendado com sucesso!")
            return render(request, 'agendamento.html')
        else:
            print(form.errors)
            messages.error(request,"Falha ao agendar, verifique os dados e tente novamente!")
            form=DadosForm()
    else:
        form = DadosForm()
    context= {
        'form': form
    }
    return render(request, 'agendamento.html', context)



def treinamento(request):
    if request.method == "POST":
        form = FormTreinamento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro feito!")
            return render(request, "treinamento.html")
        else:
            print(form.errors)
            messages.error(request, "Falha ao cadastrar verifique os dados.")
            form = FormTreinamento()
    else:
        form = FormTreinamento()

    context = {
        'form': form
    }
    return render(request, 'treinamento.html', context)

def docentes(request):
    return render(request, 'docentes.html')

def cadastrar_docente(request):
    return render(request, 'cadastrardocente.html')

def clientes(request):
    return render(request, 'cliente.html')
    

