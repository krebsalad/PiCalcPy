## PiCalcPy
Simple picalc bottle server. Meant for demonstration purpose.

# Requirements:
- python
- wget

# install the picalc server
Clone the repo, go in to the file and run: (sudo) python install_picalc.py
- requires sudo rights to install mpmath library
- will download bottle.py library
#

# install a loadbalancer
Clone the repo, go in to the file and run: (sudo) python install_picalc.py lb
- will download [PumpkinLB](https://pypi.org/project/PumpkinLB/) loadbalancing tool
#

# start the picalc server
Start the server with: (sudo) python run.py mode=server
- will listen on port 8080 tcp from 0.0.0.0
- send request from other machine: curl <host machine ip>:8080/PiCalc/1000
#
  
# start the load balancer
First change the mappings in lb_config.cfg
Start the server with: (sudo) python run.py mode=lb
- will listen on port 8080 on defined ips in lb_config.cfg and map them to 80 
- send request from other machine: curl <host machine ip>:80/PiCalc/1000
#
