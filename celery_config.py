from celery import Celery
import os

# Defina a configuração do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edados.settings')
app = Celery('edados')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carregue tarefas assíncronas de todos os aplicativos Django
app.autodiscover_tasks()

# Execute as tarefas assíncronas em tempo real
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
