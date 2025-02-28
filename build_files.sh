#!/usr/bin/env bash
echo "Instalando as dependecias"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Migrando banco de dados..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "Criando user admin"
python3 create_superuser.py