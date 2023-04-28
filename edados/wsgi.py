import os
import sys

# Adiciona o diretório do projeto no path do Python
sys.path.append('/var/www/edados')

# Ativa o ambiente virtual
activate_env=os.path.expanduser('/var/www/edados/venvteste/bin/activate_this.py')
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

# Configurações do Django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edados.settings')

application = get_wsgi_application()
