#!/bin/bash
PID=$(ps aux | grep /usr/bin/python3.5 | grep -v grep | awk '{print $2}')

if [ -z "$PID" ];
then
    exit 0
else
    kill $PID
fi

