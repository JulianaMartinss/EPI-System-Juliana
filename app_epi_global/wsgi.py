import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_epi_global.settings.dev')
application = get_wsgi_application()
