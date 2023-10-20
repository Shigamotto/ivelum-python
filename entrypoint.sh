#!/usr/bin/env bash
if [ "$1" == 'runserver' ]; then
    exec env PYTHONPATH=.:$PYTHONPATH gosu app python proxy_service/manage.py runserver 0.0.0.0:8232
fi

exec "$@"
