#!/bin/bash
pip install -e .
export FLASK_APP=flaskerino/flaskerino.py
flask run
