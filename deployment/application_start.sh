#!/bin/bash
export FLASK_APP=$(find "$(pwd -P)" -name "flaskerino.py")
/usr/local/bin/flask run --host=0.0.0.0 >/dev/null 2>&1 &

sleep 10
