#!/usr/bin/env bash
# dev-start.sh , only for test
# see https://serverfault.com/questions/870568/fatal-error-cant-open-and-lock-privilege-tables-table-storage-engine-for-use
mkdir -p app/static/chat & mkdir -p app/static/upload & mkdir -p app/static/images/avatar
python3 manage.py db upgrade
python3 manage.py runserver --host 0.0.0.0 --port 8080 --threaded
#service nginx start
#uwsgi uwsgi_config.ini
