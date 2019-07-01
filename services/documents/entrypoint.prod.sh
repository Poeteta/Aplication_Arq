#!/bin/sh
echo "Esperando a postgres..."

while ! nc -z document-db 5432; do
    sleep 0.1
done

echo "PostgreSQL inicializado"

gunicorn -b 0.0.0.0:5000 manage:app