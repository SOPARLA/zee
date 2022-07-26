# The sys library for extracting the cli args.
# To check the tool dependencies, use the check_needs library.
# colorama library for colorize terminal.
import sys
from src.general.settings import check_needs; check_needs.start()
from src.zee import run
from src.wrapper import banner
from colorama import init,Fore

init(autoreset=True)
# user commands
args = sys.argv
# allowed commands
commands = ["active","passive","version"]

# banner.banner()
# verify the length of args , if args is bigger than 1 run the tool.
if len(args) > 1:

    # if command was in allowed commands run
    if str(args[1]).lower() in commands:
        run.run(str(args[1]).lower())
    # else show the help message and error message
    else:
        banner.help_banner()
        exit(f"\n{Fore.RED}[ERROR] PLEASE CHOOSE IN WHAT MODE YOU WANT TO ENUMERATE SUBDOMAINS {Fore.WHITE}[ active , passive , version ]")

# otherwise if the args length is equal to 1, show the help message.
elif len(args) == 1:
    banner.help_banner()
    exit()