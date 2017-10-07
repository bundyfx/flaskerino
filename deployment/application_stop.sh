#!/bin/bash
kill $(ps aux | grep /usr/bin/python3.5 | grep -v grep | awk '{print $2}')
