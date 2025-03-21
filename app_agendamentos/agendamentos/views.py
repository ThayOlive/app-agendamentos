from datetime import datetime
from django.shortcuts import render, redirect
from .forms import DadosForm, FormTreinamento, FormDocente, FormCliente
from django.contrib import messages
from .models import Cliente, Treinamento, Docente, DadosGerais
from django.http import JsonResponse

def agendamento(request):  
    #pegar os dados das tabelas cliente, docente e treinamento do banco de dados 
    clientes = Cliente.objects.all()
    docentes = Docente.objects.all()
    treinamentos = Treinamento.objects.all()

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
        'form': form,
        'clientes': clientes,
        'docentes': docentes,
        'treinamentos': treinamentos,
    }
    return render(request, 'agendamento.html', context)



def treinamento(request):
    if request.method == "POST": 
        form = FormTreinamento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro feito!")
            return redirect('treinamento')
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



def cadastrar_docente(request):
    if request.method == "POST":
        form = FormDocente(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro feito!")
            return redirect('cadastrardocente')
        else:
            print(form.errors)
            messages.error(request, "Falha ao cadastrar verifique os dados.")
            form = FormDocente()
    else:
        form= FormDocente()

    context = {
        'form' : form
    }
    return render(request, 'cadastrardocente.html', context)
    

def clientes(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro feito!")
            return redirect('clientes')
        else:
            print(form.errors)
            messages.error(request, "Falha ao cadastrar verifique os dados.")
            form = FormCliente()
    else:
        form= FormCliente()

    context = {
        'form' : form
    }
            
    return render(request, 'clientes.html', context)
    

#construir visualização em forma de calendário
def calendario_agendamento(request):
    agendamentos = DadosGerais.objects.all()
    events = []

    for agendamento in agendamentos:
        event = {
            'title':f'{agendamento.treinamento.nome} - {agendamento.docente.nome} - {agendamento.cliente}',
            'start':f'{agendamento.data_inicial} - {agendamento.horas}',
            'end':f'{agendamento.data_final}',
            'description':f'{agendamento.cliente}',
            'color': 'blue'
        }
        events.append(event)
    
    context = {
        'events': events
    }
    return render(request, 'calendario_agendamento.html', context)

def obter_agendamentos(request):
    agendamentos = DadosGerais.objects.all()
    events = []

    for agendamento in agendamentos:
        start_datetime = datetime.combine(agendamento.data_inicial.date(), agendamento.horas)
        end_datetime = agendamento.data_final 
        event = {
            'title':f'{agendamento.treinamento.nome} - {agendamento.docente.nome} - {agendamento.cliente} ',
            'start': start_datetime.strftime("%Y-%m-%dT%H:%M:%S"),  # Formato ISO 8601
            'end': end_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            'description':f'{agendamento.cliente}',
            'color': 'blue'
        }
        events.append(event)

    return JsonResponse(events, safe=False)
