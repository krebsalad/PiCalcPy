# PiCalcPy
Simple picalc bottle server. Meant for demonstration purpose.

Requirements:
- python
- wget

Clone the repo, go in to the file and run: (sudo) python install_picalc_server.py
- requires sudo rights to install mpmath library
- will download bottle.py library

Start the server with: (sudo) python run.py
- will listen on port 8080 tcp from 0.0.0.0
- send request from other machine: curl <host machine ip>:8080/PiCalc/1000
