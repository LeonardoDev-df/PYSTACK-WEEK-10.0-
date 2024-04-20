# PYSTACK-WEEK-10.0

## Introdução
Este repositório contém materiais e informações para a PYSTACK-WEEK-10.0, uma semana dedicada ao aprendizado e prática de desenvolvimento em Python.

## Configuração do Ambiente

### Pré-requisitos
- Python 3.x instalado em seu sistema

### Configurando o Ambiente Virtual (venv)

#### Linux
```bash
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\Activate

Caso encontre erros de permissão, execute o seguinte comando e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Instalando Dependências

pip install django
pip install pillow


Executando o Servidor
Após configurar o ambiente e instalar as dependências, você pode executar o servidor Django com o seguinte comando:

python manage.py runserver

Isso iniciará o servidor de desenvolvimento e você poderá acessar a aplicação em seu navegador usando o endereço fornecido no terminal.
