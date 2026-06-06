#!/bin/sh

echo "Running migrations..."

export PGPASSWORD=$DB_PASSWORD

for file in /migrations/*.sql; do
  echo "Applying $file"
  psql -h db -U user -d sensors -f "$file"
done

echo "FILES:"
ls -l /migrations
echo "Migrations done. Starting app..."

exec gunicorn -w 4 -b 0.0.0.0:5000 app:app