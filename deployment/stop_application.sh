#!/bin/bash
ps aux | grep python | grep -v "grep python" | awk '{print $2}' | xargs kill -9
