# Sistema de Cadastro Hospitalar

Sistema web desenvolvido com Django para gerenciar cadastros de pacientes, médicos e consultas.  
O projeto implementa operações CRUD (Create, Read, Update, Delete) permitindo criar, visualizar, editar e excluir registros.

Este projeto foi criado com o objetivo de **praticar desenvolvimento web com Django** e conceitos de modelagem de dados.

---

## Funcionalidades

- Cadastro de Pacientes
- Cadastro de Médicos
- Registro de Consultas
- Listagem de registros
- Edição de informações
- Exclusão de dados

---

## Tecnologias utilizadas

- **Python**
- **Django**
- **HTML**
- **SQLite**

---

## Estrutura do sistema

O sistema possui três entidades principais:

**Paciente**
- Informações pessoais
- Dados médicos básicos

**Médico**
- Especialidade
- Registro profissional (CRM)

**Consulta**
- Relaciona paciente e médico
- Data da consulta
- Relatório do atendimento

---

## Fonte de estudo

A implementação das consultas e da estrutura geral do projeto foi inspirada nos exemplos e conceitos apresentados no livro:

**"Curso Intensivo de Python" (Eric Matthes)**

---

## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/Luan-tm-01/Projeto_CRUD.git
```

Entre na pasta:

```bash
cd Projeto_CRUD
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual (Windows):

```bash
venv\Scripts\activate
```

Instale o Django:

```bash
pip install django
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```
