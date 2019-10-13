# Picalc server
import os
import sys
import re
import socket
import subprocess

# vars
current_dir = os.getcwd()
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
mode = "help"
lb_config = "dont_set_config_file"

# read args
for arg in sys.argv:
    if(re.match("ip=",arg)):
        ip = re.sub("ip=", "", arg)
        if(re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)):
            ip_addr = ip

    if(re.match("mode=",arg)):
        txt = re.sub("mode=", "", arg)
        if(txt == "lb"):
            mode = "lb"
        if(txt == "server"):
            mode = "server"
    
    if(re.match("lb_config=",arg)):
        txt = re.sub("lb_config=", "", arg)
        lb_config = txt

# help
if(mode == "help"):
    print("run with arguments  ( mode=server ) or ( mode=lb ), also, in lb mode you can set PumpkinLB config with ( lb_config=configcontents ) ")
    sys.exit()        
        
## Loadbalancer ##
if(mode == "lb"):
    # if set new config file
    if(lb_config != "dont_set_config_file"):
        config_file = open("lb_config.cfg", "w")
        config_file.write(lb_config)
        config_file.close()
    # start loadbalancer
    subprocess.call(["PumpkinLB-2.0.0/PumpkinLB.py", "lb_config.cfg"], cwd=current_dir)
    sys.exit()


## Picalc server ##
if(mode != "server"):
    print("no such mode " + mode)
    sys.exit()
    


