web: gunicorn blog_project.blog_project.wsgi:application --log-file -
--log-level debug
python manage.py collectstatic -noinput 
manage.py migrate