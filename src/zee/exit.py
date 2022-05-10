# platform library used to obtain client distribution.
# subprocess library for terminate tool in windows distribution.
# os library for get tool pid and terminate tool in linux distribution.
# colorama library for text coloring.
from platform import system
from subprocess import getoutput
from os import getpid,kill
from colorama import Fore

# terminate_tool function to terminate the tool with a given pid.
def terminate_tool():
    opt = system().lower()
    pid = getpid()
    if opt == "windows":
        getoutput(f"taskkill /T /F /PID {pid}")
    elif opt == "linux":
        getoutput(f"pkill -n -x -i -u {pid}")
    else:
        kill(pid,9)

# show the warning message  with the close_message function, then terminate the tool with the terminate_tool function.
def closed_message():
    print(Fore.RED+"\n\nPROGRAM HAS BEEN CLOSED")
    terminate_tool()