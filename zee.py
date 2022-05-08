import sys
from src.wrapper import argumants
from src.zee import check_args

try:
    from colorama import Fore,init
    init(autoreset=True)
except ModuleNotFoundError:
    exit("[ERROR] MODULE NOT FOUND\nPLEASE INSTALL colorama MODULE\n\teg. pip install colorama")


args = argumants.get_args()[0]

if args.toolversion:
    sys.exit(Fore.RED+"VERSION: 1.0\n")

if args.simple_save:
    if not args.simple_save.endswith(".txt"):
        exit(Fore.RED+f"\n\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY TXT FILES")
    out = f"{args.simple_save}:simple"

elif args.advanced_save:
    if not args.advanced_save.endswith(".txt"):
        exit(Fore.RED+f"\n\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY TXT FILES")
    out = f"{args.advanced_save}:advanced"
else:
    out = False

if args.configfile:
    if not str(args.configfile).lower().endswith(".ini"):
        sys.exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY INI FILES\n")

# CHECK THE USER ARGUMANTS
check_args.check(args.wordlist,args.URL,args.configfile,args.header,args.filterstatus,args.httpmethod,args.timeout,args.filterlength,args.thread,args.silent,args.color,out)