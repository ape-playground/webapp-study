#!/bin/sh
gunicorn main:app -c "config/gunicorn.config.py"
exec "$@"
