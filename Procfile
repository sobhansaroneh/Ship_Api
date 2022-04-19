web: python manage.py runserver 0.0.0.0:%PORT%
web: gunicorn ship.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput