from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create new users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Set a username to a new user.')
        parser.add_argument('email', type=str, help='Set a email to a new user.')
        parser.add_argument('password', type=str, help='Set a password to a new user.')

        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        admin = kwargs['admin']

        if admin:
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            User.objects.create_user(username=username, email=email, password=password)

        self.stdout.write(self.style.SUCCESS(f"New user has been created with the following data:"))
        self.stdout.write(self.style.SUCCESS(f"Username: {username}"))
        self.stdout.write(self.style.SUCCESS(f"Email: {email}"))
        self.stdout.write(self.style.SUCCESS(f"Password: {password}"))
