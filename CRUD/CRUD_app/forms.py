from django import forms
from .models import DadosMedico, DadosPaciente, Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = DadosPaciente
        fields = ['nome_completo','data_nascimento','sexo','cpf','telefone','email','endereco','contato_emergencia','observacoes']
        labels = {'nome_completo': 'Nome Completo ',
                  'data_nascimento': 'Data de Nascimento ',
                  'sexo': 'Sexo ',
                  'cpf': 'CPF ',
                  'telefone': 'Telefone de Contato',
                  'email': 'E-mail ',
                  'endereco': 'Endereço ',
                  'contato_emergencia': 'Contato de Emergência ',
                  'observacoes': 'Observações'}
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = DadosMedico
        fields = ['nome_completo', 'cpf', 'telefone', 'email', 'especialidade', 'crm', 'data_contratacao', 'turno']
        labels = {'nome_completo': 'Nome Completo',
                  'cpf': 'CPF',
                  'telefone': 'Telefone',
                  'email': 'E-mail',
                  'especialidade': 'Especialidade',
                  'crm': 'CRM',
                  'turno': 'Turno',
                  'data_contratacao': 'Data da Contratação'}
        widgets = {
            'data_contratacao': forms.DateInput(attrs={'type': 'date'}),
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data_consulta', 'hora_consulta', 'motivo_consulta', 'relatorio', 'status_consulta']
        labels = {'paciente': 'Paciente',
                  'medico': 'Médico',
                  'data_consulta': 'Data da Consulta',
                  'hora_consulta': 'Hora da Consulta',
                  'motivo_consulta': 'Motivo da Consulta',
                  'relatorio' : 'Relátorio da Consulta',
                  'status_consulta': 'Status da Consulta'}
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
            'hora_consulta': forms.TimeInput(attrs={'type': 'time'}),
        }