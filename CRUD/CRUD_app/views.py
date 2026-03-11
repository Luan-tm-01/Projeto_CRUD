from django.shortcuts import render
from .models import DadosPaciente, DadosMedico, Consulta
from .forms import PacienteForm, MedicoForm, ConsultaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

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

def edit_paciente(request, paciente_id):
    paciente = DadosPaciente.objects.get(id=paciente_id)
    if request.method != 'POST':
        form = PacienteForm(instance=paciente)
    else:
        form = PacienteForm(instance=paciente, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('paciente', args=[paciente.id]))
    context = {'paciente': paciente, 'form': form}

    return render(request, 'CRUD_app/edit_paciente.html', context)

def delete_paciente(request, paciente_id):
    paciente = DadosPaciente.objects.get(id=paciente_id)

    if request.method == "POST":
        paciente.delete()
        return redirect('pacientes')

def medicos(request):
    medicos = DadosMedico.objects.order_by('nome_completo')
    context = {'medicos' : medicos}
    return render(request, 'CRUD_app/medicos.html', context)

def medico(request, medico_id):
    medico = DadosMedico.objects.get(id=medico_id)
    context = {'medico': medico}
    return render(request, 'CRUD_app/medico.html', context)

def novo_medico(request):
    if request.method != 'POST':
        form = MedicoForm
    else:
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medicos'))
    context = {'form': form}
    return render(request, 'CRUD_app/novo_medico.html', context)

def edit_medico(request, medico_id):
    medico = DadosMedico.objects.get(id=medico_id)
    if request.method != 'POST':
        form = MedicoForm(instance=medico)
    else:
        form = MedicoForm(instance=medico, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medico', args=[medico.id]))
    context = {'medico': medico, 'form': form}

    return render(request, 'CRUD_app/edit_medico.html', context)

def delete_medico(request, medico_id):
    medico = DadosMedico.objects.get(id=medico_id)

    if request.method == "POST":
        medico.delete()
        return redirect('medicos')

def consultas(request):
    consultas = Consulta.objects.order_by('data_consulta')
    context = {'consultas': consultas}
    return render(request, 'CRUD_app/consultas.html', context)

def consulta(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    context = {'consulta': consulta}
    return render(request, 'CRUD_app/consulta.html', context)

def nova_consulta(request):
    if request.method != 'POST':
        form = ConsultaForm
    else:
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('consultas'))
    context = {'form': form}
    return render(request, 'CRUD_app/nova_consulta.html', context)

def edit_consulta(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    if request.method != 'POST':
        form = ConsultaForm(instance=consulta)
    else:
        form = ConsultaForm(instance=consulta, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('consulta', args=[consulta.id]))
    context = {'consulta': consulta, 'form': form}

    return render(request, 'CRUD_app/edit_consulta.html', context)

def delete_consulta(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)

    if request.method == "POST":
        consulta.delete()
        return redirect('consultas')