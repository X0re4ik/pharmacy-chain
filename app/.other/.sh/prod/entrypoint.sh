#! /bin/sh
python manage.py collectstatic --noinput && python manage.py migrate --noinput

if [ ! -f "/init_file._pharmacy_chain.txt" ]; then
    touch > init_file._pharmacy_chain.txt
    python manage.py loaddata .other/_data/_data.json
fi

gunicorn -b "0.0.0.0:8000" --access-logfile - app.wsgi:application