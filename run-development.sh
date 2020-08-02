#! /usr/bin/env bash


docker run --rm -p 5000:5000 -e FLASK_ENV=development -v "$PWD/flaskapi:/app" cyberbionicus
