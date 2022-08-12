# platform library used to obtain client distribution.
# subprocess library for terminate tool in windows distribution.
# os library for get tool pid and terminate tool in linux distribution.
from platform import system
from subprocess import getoutput
from os import getpid,kill

# terminate_tool function to terminate the tool with a given pid.
def terminate_tool():
    print()
    opt = system().lower()
    pid = getpid()
    if opt == "windows":
        getoutput(f"taskkill /T /F /PID {pid}")
    elif opt == "linux":
        getoutput(f"pkill -n -x -i -u {pid}")
    else:
        kill(pid,9)