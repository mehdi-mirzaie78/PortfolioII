from home.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = settings.SUPERUSER_USERNAME
        email = settings.SUPERUSER_EMAIL
        try:
            if not User.objects.filter(username=username).exists() and not User.objects.filter(
                is_superuser=True).exists():
                print("admin user not found, creating one")
                new_password = settings.SUPERUSER_PASSWORD
                u = User.objects.create_superuser(username, email, new_password)
                print(f"===================================")
                print(f"A superuser '{username}' was created with password '{new_password}'")
                print(f"===================================")
            else:
                print("admin user found. Skipping super user creation")

        except Exception as e:
            print(f"There was an error: {e}")
