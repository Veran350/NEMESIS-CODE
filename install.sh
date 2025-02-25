#!/bin/bash  
termux-wake-lock  
pkg update -y  
pkg install -y python php metasploit git  
pip install flask scapy  
git clone https://github.com/yourusername/NEMESIS-CODE  
cd NEMESIS-CODE  
chmod +x auto/*.sh  
./auto/apk_generator.sh  
mv auto/termux_boot.service $PREFIX/etc/init.d/  
termux-reload-settings  
php -S 0.0.0.0:8080 -t web/ &  
python core/termux_automator.py  
