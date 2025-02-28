import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User.objects.create_superuser('admin', 'admin@example.com', 'admin')
print("Superusuário criado com sucesso!")