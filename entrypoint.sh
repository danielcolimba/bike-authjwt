#!/bin/bash
set -e

# Configurar el módulo de settings de Django
export DJANGO_SETTINGS_MODULE=authservice.settings

echo "Esperando a que la base de datos esté disponible..."
until PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c '\q' 2>/dev/null; do
  echo "Base de datos no disponible - esperando..."
  sleep 2
done
echo "Base de datos disponible!"

# Nota: Las migraciones se ejecutarán manualmente
echo "Para ejecutar migraciones, usar: docker exec <container> python manage.py migrate"

# Iniciar el servidor directamente
echo "Iniciando servidor en puerto 8001..."
exec gunicorn authservice.wsgi:application --bind 0.0.0.0:8001 --workers 3 --timeout 60