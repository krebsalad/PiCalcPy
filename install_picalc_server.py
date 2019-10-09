import os
import subprocess

current_dir = os.getcwd()
pi_calc_dir = current_dir + "/"
subprocess.call(["wget", "https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py"], cwd=pi_calc_dir)
subprocess.call(["wget","https://files.pythonhosted.org/packages/ca/63/3384ebb3b51af9610086b23ea976e6d27d6d97bf140a76a365bd77a3eb32/mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
subprocess.call(["tar", "-xzf", "mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
subprocess.call(["python", "setup.py", "install"], cwd=str(pi_calc_dir+"mpmath-1.1.0"))
subprocess.call(["rm", "mpmath-1.1.0.tar.gz"], cwd=pi_calc_dir)
