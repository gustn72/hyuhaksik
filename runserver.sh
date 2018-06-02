#!/bin/sh

RootDir="/volume1/web/dj"
DB_FILE=${RootDir}/db.sqlite3
LOG="${RootDir}/log/Runserver.log"

if [ -f "$DB_FILE" ]; then
    rm $DB_FILE
fi

python3 ${RootDir}/manage.py makemigrations >>${LOG}
python3 ${RootDir}/manage.py migrate >>${LOG}
python3 ${RootDir}/manage.py runserver 0.0.0.0:8000 >>${LOG}
