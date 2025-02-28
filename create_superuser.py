from django.conf import settings

settings.configure()

from django.contrib.auth.models import User

user = User.objects.get(username='admin')

user.set_password('admin')

user.save()