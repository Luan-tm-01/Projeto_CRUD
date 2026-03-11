from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientes/<paciente_id>/', views.paciente, name='paciente'),
    path('novo_paciente', views.novo_paciente, name='novo_paciente'),
    path('edit_paciente/<paciente_id>', views.edit_paciente, name='edit_paciente'),
    path('pacientes/<paciente_id>/delete/', views.delete_paciente, name='delete_paciente'),

    path('medicos', views.medicos, name='medicos'),
    path('medicos/<medico_id>/', views.medico, name='medico'),
    path('novo_medico', views.novo_medico, name='novo_medico'),
    path('edit_medico/<medico_id>', views.edit_medico, name='edit_medico'),
    path('medicos/<medico_id>/delete/', views.delete_medico, name='delete_medico'),

    path('consultas', views.consultas, name='consultas'),
    path('consultas/<consulta_id>/', views.consulta, name='consulta'),
    path('nova_consulta', views.nova_consulta, name='nova_consulta'),
    path('edit_consulta/<consulta_id>', views.edit_consulta, name='edit_consulta'),
    path('consultas/<consulta_id>/delete/', views.delete_consulta, name='delete_consulta'),
]