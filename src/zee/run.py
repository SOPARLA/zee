# colorama library for colorize terminal.
# request library for getting the current tool version from github.
from colorama import Fore
from requests import get
from src.wrapper import argumants
from src.zee.active import check_args as active_check
from src.zee.passive import check_args as passive_check

# This is the main function. This function checks the user arguments that are used and runs that section.
def run(arg):
    if arg == "version":
        with open("src/general/version.txt","r") as tool_version:
            exit(check_version(tool_version.read()))
    
    elif arg ==  "active":
        active()
   
    elif arg ==  "passive":
        passive()


# This function checks the tool version.
def check_version(current_version):
    ver = get("https://raw.githubusercontent.com/SOPARLA/zee/master/src/general/version.txt").text
    if ver == current_version:
        return F"\n{Fore.LIGHTGREEN_EX}{current_version} UP TO DATE"
    else:
        return F"\n{Fore.LIGHTRED_EX}{current_version} THE TOOL IS NOT UP TO DATE ( NEW: {ver} )"


# This function runs the active section.
def active():
    # This variable will contain the arguments that were used.
    args = argumants.get_active_args()[0]
    
    # By default out is False ( out = write tool output to the file. )
    out = False


    # If the -o option was used, this will check the output file extension.
    if args.out:
        if not str(args.out).lower().endswith(".txt"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION PLEASE PROVED ONLY TXT FILES\n\t{Fore.WHITE}eg. python zee.py active -o out.txt")
        out = f"{args.out}:simple"

    # If the -od option was used, this will check the output file extension.
    if args.det:
        if not str(args.det).lower().endswith(".txt"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION PLEASE PROVED ONLY TXT FILES\n\t{Fore.WHITE}eg. python zee.py active -or out.txt")
        out = f"{args.det}:detail"

    # If the -oj option was used, this will check the output file extension.
    elif args.json:
        if not str(args.json).lower().endswith(".json"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION PLEASE PROVED ONLY JSON FILES\n\t{Fore.WHITE}eg. python zee.py active -oj out.txt")
        out = f"{args.json}:json"

    # If -config was specified, this will check the output file extension.
    if args.configfile:
        if not str(args.configfile).lower().endswith(".ini"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY INI FILES\n")

    # Determines whether or not the URL is specified.
    if not args.URL:
        exit(Fore.RED+f"\n[ERROR] PLEASE SPECIFY THE TARGET URL\n\t{Fore.WHITE}eg. python zee.py -u https://zee.domain.com\n")

    # CHECK THE USER ARGUMANTS
    active_check.check(args.wordlist,args.URL,args.configfile,args.header,args.filterstatus,args.httpmethod,args.timeout,args.filterlength,args.thread,args.silent,args.color,out)


# This function runs the passive section.
def passive():
    args = argumants.get_passive_args()[0]

    # By default out is False ( out = write tool output to the file. )
    out = False

    # If the -o option was used, this will check the output file extension.
    if args.raw:
        if not str(args.raw).lower().endswith(".txt"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION PLEASE PROVED ONLY TXT FILES\n\t{Fore.WHITE}eg. python zee.py passive -or out.txt")
        out = f"{args.raw}:raw"

    # If the -oj option was used, this will check the output file extension.
    elif args.json:
        if not str(args.json).lower().endswith(".json"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION PLEASE PROVED ONLY JSON FILES\n\t{Fore.WHITE}eg. python zee.py passive -oj out.txt")
        out = f"{args.json}:json"

    # If -config was specified, this will check the output file extension.
    if args.configfile:
        if not str(args.configfile).lower().endswith(".ini"):
            exit(Fore.RED+f"\n[ERROR] WRONG FILE EXTENSION\nPLEASE PROVED ONLY INI FILES\n")

    # If verbose mode and silent mode are specified together, the tool will show this error.
    if args.verb and args.silent:
        exit(Fore.RED+"\n[ERROR] YOU CAN'T DO VERBOSE MODE WITH SILENT MODE.\n")

    # If a single URL and a list of URLs are specified together, the tool will show this error.
    if args.URL and args.URL_LIST:
        exit(Fore.RED+f"\n[ERROR] PLEASE DO NOT SPECIFY THE TARGET URL OR THE TARGET FILE AT THE SAME TIME\n\t{Fore.WHITE}eg. python zee.py -u domain.com {Fore.RED}or {Fore.WHITE}python zee.py -ul urls.txt\n")
    else:
        if not args.URL and not args.URL_LIST:
            exit(Fore.RED+f"\n[ERROR] PLEASE SPECIFY THE TARGET URL OR TARGET URLS\n\t{Fore.WHITE}eg. python zee.py -u domain.com {Fore.RED}or {Fore.WHITE}python zee.py -ul urls.txt\n")

    # CHECK THE USER ARGUMANTS
    passive_check.check(args.URL_LIST,args.URL,args.configfile,args.thread,args.check_live,args.filterstatus,args.filterlength,args.silent,args.color,out,args.verb)