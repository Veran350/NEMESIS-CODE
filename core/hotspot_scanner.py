import subprocess  
import json  
import time  

def scan_devices():  
    try:  
        arp = subprocess.check_output("arp -n", shell=True).decode()  
        devices = []  
        for line in arp.splitlines()[1:]:  
            if len(line.split()) >= 3:  
                ip, mac = line.split()[0], line.split()[2]  
                vendor = subprocess.getoutput(f"curl -s https://api.macvendors.com/{mac}")  
                devices.append({"ip": ip, "mac": mac, "vendor": vendor})  
        with open("web/devices.json", "w") as f:  
            json.dump(devices, f)  
    except: pass  

while True:  
    scan_devices()  
    time.sleep(5)  
