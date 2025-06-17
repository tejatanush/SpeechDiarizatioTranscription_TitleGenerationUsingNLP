import os
import django
from django.core.management import execute_from_command_line
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
execute_from_command_line(['manage.py', 'runserver', '8000'])