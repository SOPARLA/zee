import sys
try:
    from colorama import Fore,init
    init(autoreset=True)
except ModuleNotFoundError:
    exit("\033[91m\n[ERROR] MODULE NOT FOUND\nPLEASE INSTALL colorama MODULE\n\teg. pip install colorama\n")
from src.wrapper import argumants
from src.zee import check_args

args = argumants.get_args()[0]

if args.toolversion:
    sys.exit(Fore.RED+"\nVERSION: 1.0\n")

if args.simple_save:
    if not args.simple_save.endswith(".txt"):
        exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY TXT FILES\n")
    out = f"{args.simple_save}:simple"

elif args.advanced_save:
    if not args.advanced_save.endswith(".txt"):
        exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY TXT FILES\n")
    out = f"{args.advanced_save}:advanced"
else:
    out = False

if args.configfile:
    if not str(args.configfile).lower().endswith(".ini"):
        sys.exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY INI FILES\n")

if not args.URL:
    exit(Fore.RED+f"\n[ERROR] PLEASE SPECIFY THE TARGET URL\n\t{Fore.WHITE}eg. python zee.py -u https://zee.domain.com\n")

# CHECK THE USER ARGUMANTS
check_args.check(args.wordlist,args.URL,args.configfile,args.header,args.filterstatus,args.httpmethod,args.timeout,args.filterlength,args.thread,args.silent,args.color,out)