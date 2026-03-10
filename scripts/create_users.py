import os
import sys

# Set up the Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django

django.setup()

from app.models.user_models import User

users = [
    {
        "email": "admin@email.com",
        "name": "admin",
        "password": "1234",
        "is_superuser": True,
        "is_staff": True
    },
    {
        "email": "funcionario@email.com",
        "name": "Funcionario",
        "password": "1234",
        "is_superuser": False,
        "is_staff": True
    },
    {
        "email": "a@email.com",
        "name": "Usuario A",
        "password": "1234",
        "is_superuser": False,
        "is_staff": False
    },
    {
        "email": "b@email.com",
        "name": "Usuario B",
        "password": "1234",
        "is_superuser": False,
        "is_staff": False
    },
    {
        "email": "c@email.com",
        "name": "Usuario C",
        "password": "1234",
        "is_superuser": False,
        "is_staff": False
    },
]

for data in users:
    user = User.objects.create(
       email=data['email'], 
       name=data['name'],
       is_superuser=data['is_superuser'],
       is_staff=data['is_staff'],
       is_active=True
    )

    user.set_password(data['password'])
    user.save()