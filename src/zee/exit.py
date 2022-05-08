from platform import system
from subprocess import getoutput
from os import getpid,kill
from colorama import Fore

def killproc():
    opt = system().lower()
    pid = getpid()
    if opt == "windows":
        getoutput(f"taskkill /T /F /PID {pid}")
    elif opt == "linux":
        getoutput(f"pkill -n -x -i -u {pid}")
    else:
        kill(pid,9)

def mes():
    print(Fore.RED+"\n\nPROGRAM HAS BEEN CLOSED")
    killproc()