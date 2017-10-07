#!/bin/bash
PID=$(ps aux | grep /usr/local/bin/flask | grep -v grep | awk '{print $2}')

if [ -z "$PID" ];
then
    exit 0
else
    kill $PID >/dev/null 2>&1
    exit 0
fi

