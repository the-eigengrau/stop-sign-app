#!/usr/bin/env bash

docker run --rm -p 5000:5000 -e FLASK_ENV=production cyberbionicus gunicorn api:app
