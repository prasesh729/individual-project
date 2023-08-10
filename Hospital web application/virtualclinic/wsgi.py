import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtualclinic.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root="/path/to/static/files")
application.add_files(os.path.join(BASE_DIR, '/media/'), prefix='more-files/')
