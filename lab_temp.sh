#!/bin/bash

while true; do 
   patchpanel_temp=$(snmpget -v 2c -c public labenv .1.3.6.1.4.1.17095.3.2.0 | cut -d'"' -f2)
   echo "put labroom.temperature $(date +%s) $patchpanel_temp host=labroom sensor=patchpanel"
   #echo "put labroom.temperature $(date +%s) $patchpanel_temp host=labroom sensor=patchpanel" | nc localhost 4242
   sleep 10
done | nc -w 20 localhost 4242


