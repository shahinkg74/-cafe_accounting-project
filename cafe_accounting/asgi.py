import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafe_accounting.settings')

appilication = get_asgi_application()