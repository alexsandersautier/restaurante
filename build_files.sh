#!/bin/bash

# Atualiza o pip
python -m ensurepip --default-pip
python -m pip install --upgrade pip

# Instala as dependências do projeto
pip install -r requirements.txt

# Coleta os arquivos estáticos
python restaurante/manage.py collectstatic --noinput
