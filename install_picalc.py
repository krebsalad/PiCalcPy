# picalc server installer

import os
import subprocess
import sys

# vals
current_dir = os.getcwd()
pi_calc_dir = current_dir + "/"

# install loadbalancer if arg lb
if(len(sys.argv) > 1):
   arg = sys.argv[1]
   if(arg == "lb"):
        subprocess.call(["wget", "https://files.pythonhosted.org/packages/cc/88/b4df1a3416ea09dd17bea4214d802d87f83afeafe9646ef42712c8e652f6/PumpkinLB-2.0.0.tar.gz"], cwd=pi_calc_dir)
        subprocess.call(["tar", "-xzf", "PumpkinLB-2.0.0.tar.gz"], cwd=pi_calc_dir)
        subprocess.call(["rm", "PumpkinLB-2.0.0.tar.gz"], cwd=pi_calc_dir)
        sys.exit()

# or else install the server
subprocess.call(["wget", "https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py"], cwd=pi_calc_dir)
subprocess.call(["wget","https://files.pythonhosted.org/packages/ca/63/3384ebb3b51af9610086b23ea976e6d27d6d97bf140a76a365bd77a3eb32/mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
subprocess.call(["tar", "-xzf", "mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
subprocess.call(["python", "setup.py", "install"], cwd=str(pi_calc_dir+"mpmath-1.1.0"))
subprocess.call(["rm", "mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
print("dowloaded python mpmath lib, bottle.py")
sys.exit()

