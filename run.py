from bottle import route, run, template
from mpmath import mp

@route('/PiCalc/<p>')
def index(p):
    precision = int(p)
    if(str(type(precision)) != "<type 'int'>"):
        print(str(type(precision)))
        return str("error, precision was not an int")
    mp.dps = precision
    pi = mp.pi
    return str("PI: " + str(pi) + “\n”) 

# run
run(host='0.0.0.0', port=8080)
