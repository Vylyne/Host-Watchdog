#!/bin/bash

# Swap out the old generic /dev/ttyACM0 line for your permanent ID pointer
PORT="/dev/serial/by-id/usb-CustomWatchdog_SV08_Power_Watchdog_K762908DF12A-if00"

stty -F $PORT 115200

echo "BOOTING" > $PORT

until curl -s http://localhost:7125/printer/info | grep -q "hostname"; do
    sleep 2
done

while true; do
    echo "READY" > $PORT
    sleep 2
done
