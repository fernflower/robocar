#!/bin/bash

TTY="${tty:-/dev/ttyUSB0}"
ALLOWED='*.py *.html'

for pyfile in $(ls $ALLOWED); do
    ampy  --port "$TTY" put $pyfile
done
