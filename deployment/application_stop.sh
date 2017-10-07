#!/bin/bash
PID=$(ps aux | grep /usr/bin/python3.5 | grep -v grep | awk '{print $2}')

re='^[0-9]+([.][0-9]+)?$'
if ! [[ $PID =~ $re ]] ; then
    exit 0
else
    kill $PID >/dev/null 2>&1
    exit 0
fi

