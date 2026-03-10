from django import forms
from .models import DadosMedico, DadosPaciente, Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = DadosPaciente
        fields = ['nome_completo','data_nascimento','sexo','cpf','telefone','email','endereco','tipo_sangue','contato_emergencia','observacoes']
        labels = {'nome_completo': 'Nome Completo ',
                  'data_nascimento': 'Data de Nascimento ',
                  'sexo': 'Sexo ',
                  'cpf': 'CPF ',
                  'telefone': 'Telefone de Contato',
                  'email': 'E-mail ',
                  'endereco': 'Endereço ',
                  'tipo_sangue': 'Tipo Sanguíneo ',
                  'contato_emergencia': 'Contato de Emergência ',
                  'observacoes': 'Observações'}

#class MedicoForm

#classConsultaForm