web: celery -A myportfoilio.celery worker -l info --pool=solo -E & python manage.py migrate && python manage.py collectstatic --no-input && gunicorn dumz_exchange.wsgi