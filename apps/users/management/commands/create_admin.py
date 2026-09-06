from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        username = input('Username: ')
        email = input('Email: ')
        password = input('Password: ')
        confirm_password = input('confirm_password: ')

        if password != confirm_password:
            self.stdout.write(self.style.ERROR('Passwords do not match'))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write('User already exits')
            return

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role_type = 'ADMID'
        )

        self.stdout.write('Admin create successfully')


