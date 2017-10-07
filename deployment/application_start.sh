#!/bin/bash
export FLASK_APP=$(find "$(pwd -P)" -name "flaskerino.py")
/usr/local/bin/flask run --host=0.0.0.0 &

if [ $? == 0 ]; then
    exit 0
else
    exit 1
fi
