"""
Cấu hình cho ASGI cho project 

Với biến cấp module là applicattion
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelryshop.settings')

application = get_asgi_application()
