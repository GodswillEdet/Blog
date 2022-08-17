import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/home/ashish/Documents/Django/blog/blog_project/"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_project.settings'

application = get_wsgi_application()