#!/bin/bash

echo "Creating virtualenv"
exec virtualenv -p python3 env
source ./env/bin/activate
echo "virtual environment started"

exec pip install -r ../.require/requirements.txt
exec cd ..
exec pip install -e .