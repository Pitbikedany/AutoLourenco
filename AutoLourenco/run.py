import os
import sys

# Defina as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoLourenco.settings')

# Configure o Django
import django
django.setup()

# Importe e execute o servidor de desenvolvimento do Django
from django.core.management import execute_from_command_line
execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:8000'])
