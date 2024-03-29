from bottle import route, run, template
from mpmath import mp
import socket
import time

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

@route('/PiCalc/<p>')
def index(p):
    # set time
    start_time = time.time()
    
    # read
    precision = int(p)

    # handle non ints
    if(str(type(precision)) != "<type 'int'>"):
        print(str(type(precision)))
        return str("error, precision was not an int")

    # set precision val and calculate pi
    mp.dps = precision
    pi = mp.pi

    # end time
    processing_time = time.time() - start_time
    
    # return txt
    return str("Server ip: "+ip_addr+ "\nTime took: "+ str(processing_time) + " seconds\nPI = " + str(pi) + "\n")

# run picalc on port 8080
def run_server(port_num=8080):
    run(host=ip_addr, port=port_num)
