from django.shortcuts import render
from .models import DadosPaciente
from .forms import PacienteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def inicial(request):
    return render(request, 'CRUD_app/inicial.html')

def pacientes(request):
    pacientes = DadosPaciente.objects.order_by('nome_completo')
    context = {'pacientes' : pacientes}
    return render(request, 'CRUD_app/pacientes.html', context)

def paciente(request, paciente_id):
    paciente = DadosPaciente.objects.get(id=paciente_id)
    context = {'paciente': paciente}
    return render(request, 'CRUD_app/paciente.html', context)

def novo_paciente(request):
    if request.method != 'POST':
        form = PacienteForm
    else:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pacientes'))
    context = {'form': form}
    return render(request, 'CRUD_app/novo_paciente.html', context)