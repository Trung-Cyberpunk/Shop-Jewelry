"""
Cấu hình cho WGSI cho project

https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelryshop.settings')

application = get_wsgi_application()
