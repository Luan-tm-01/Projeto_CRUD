from django.db import models


class DadosPaciente(models.Model):
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro')
        ]
    )
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    contato_emergencia = models.CharField(max_length=11)
    observacoes = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dados dos Pacientes'

    def __str__(self):
        return f'{self.nome_completo}'


class DadosMedico(models.Model):
    nome_completo = models.CharField(max_length=150)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

    especialidade = models.CharField(
        max_length=2,
        choices=[
            ('CG', 'Clínico Geral'),
            ('CD', 'Cardiologia'),
            ('PD', 'Pediatria'),
            ('OR', 'Ortopedia'),
            ('NE', 'Neurologia'),
            ('GO', 'Ginecologia'),
            ('DE', 'Dermatologia'),
        ]
    )
    crm = models.CharField(max_length=10)
    data_contratacao = models.DateField()
    turno = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Manhã'),
            ('T', 'Tarde'),
            ('N', 'Noite'),
        ]
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dados dos Medicos'

    def __str__(self):
        return f'{self.nome_completo} - {self.get_especialidade_display()} ({self.get_turno_display()})'


class Consulta(models.Model):
    paciente = models.ForeignKey(DadosPaciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(DadosMedico, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    hora_consulta = models.TimeField()
    motivo_consulta = models.CharField(max_length=300)
    relatorio = models.TextField()
    status_consulta = models.CharField(
        max_length=1,
        choices=[
            ('R', 'Revogada'),
            ('P', 'Pendente'),
            ('C', 'Concluída'),
        ]
    )
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.medico.nome_completo} {self.data_consulta} ({self.hora_consulta})'
