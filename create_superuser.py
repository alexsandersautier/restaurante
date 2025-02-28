import django
django.setup()

from django.contrib.auth.models import User

User.objects.create_superuser('admin', 'admin@example.com', 'senha123')
print("Superusuário criado com sucesso!")
