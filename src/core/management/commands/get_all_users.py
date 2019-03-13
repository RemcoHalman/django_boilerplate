from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

users = User.objects.all()

class Command(BaseCommand):
    help = 'Get a list of all users with id'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        for user in users:
            self.stdout.write(self.style.HTTP_INFO(f"Name: {user.username}, ID: {user.id}, Email: {user.email}"))
