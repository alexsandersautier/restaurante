import django
django.setup()

from django.contrib.auth.models import User

User.objects.create_superuser('administrador', 'administrador@example.com', 'Admin@123')
print("Superusuário criado com sucesso!")
