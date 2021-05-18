#!/bin/bash
FLASK_APP=main.py flask db migrate
FLASK_APP=main.py flask db upgrade