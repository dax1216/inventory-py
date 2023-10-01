#!/bin/sh

echo "Apply migrations"

python manage.py migrate

python manage.py collectstatic --noinput

exec "$@"