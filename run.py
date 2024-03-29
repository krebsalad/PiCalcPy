# Picalc server
import os
import sys
import re
import subprocess

# vars
current_dir = os.getcwd()
mode = "help"
lb_config = "dont_set_config_file"
port_num=8080

# read args
for arg in sys.argv:
    if(re.match("mode=",arg)):
        txt = re.sub("mode=", "", arg)
        if(txt == "lb"):
            mode = "lb"
        if(txt == "server"):
            mode = "server"
    
    if(re.match("lb_config=",arg)):
        txt = re.sub("lb_config=", "", arg)
        lb_config = txt
        
    if(re.match("port=",arg)):
        txt = re.sub("port=", "", arg)
        port_num = int(txt)

        
# help
if(mode == "help"):
    print("PicalcPy: run with arguments  ( mode=server ) or ( mode=lb ), also,\n - in server mode you can add port argument example (port=8080)\n - in lb mode you can set PumpkinLB config with ( lb_config=configcontents ) ")
    sys.exit()        
        
## start Loadbalancer ##
if(mode == "lb"):
    # if set new config file
    if(lb_config != "dont_set_config_file"):
        config_file = open("lb_config.cfg", "w")
        config_file.write(lb_config)
        config_file.close()
    # start loadbalancer
    subprocess.call(["PumpkinLB-2.0.0/PumpkinLB.py", "lb_config.cfg"], cwd=current_dir)
    sys.exit()

    
## start Picalc server ##
if(mode == "server"):
    import picalc_server
    picalc_server.run_server(port_num)    
    
print("no such mode: " + mode)
sys.exit()
    


