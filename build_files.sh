#!/usr/bin/env bash
echo "Instalando as dependecias"
python -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Migrando banco de dados..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

# echo "Criando user admin"
# python3 manage.py createsuperuser --noinput --username alexsander --email alexsander@admin.com
# python3 create_superuser.py

echo "rodando as fixture"
python3 manage.py loaddata categories.json
python3 manage.py loaddata dishes.json