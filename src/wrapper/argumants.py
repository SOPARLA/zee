# In this section, we set the args

# Importing the needed libraries
# argparse for set the needed arguments
# colorama library for colorize terminal.
import argparse,sys
from argparse import SUPPRESS
from argparse import RawTextHelpFormatter
from colorama import Fore

def get_active_args():
    # set main parser
    parser = argparse.ArgumentParser(usage=SUPPRESS,formatter_class=RawTextHelpFormatter,exit_on_error=False,add_help=False,description=Fore.CYAN+f"")
    parser._action_groups.pop()

    hl = parser.add_argument_group("HELP")
    tl_com = parser.add_argument_group('ACTIVE OPTIONS')
    hp_com = parser.add_argument_group('HTTP OPTIONS')
    fl_com = parser.add_argument_group('FILTER')
    op_com = parser.add_argument_group('OUTPUT')

    # -u arg ( Specify the target url for subdomain enumeration. ) eg. -u https://zee.domain.com
    tl_com.add_argument("-u",metavar="TARGET",type=str,dest="URL",help="TARGET URL eg. -u https://ZEE.domain.com/ | https://ZEE.subdomain.domain.com/\n( PLEASE PUT ZEE IN THE PART THAT YOU WANT TO BRUTE FORCE )\n\n")
    # -w arg ( Specify the wordlist for subdomain enumeration. default set to ( seclist-20000 ) ) eg. -w subdomains.txt
    tl_com.add_argument("-w",dest="wordlist",default="def",help="\nWORDLIST PATH eg. -w path/subdomains.txt ( DEFAULT: SECLIST-20000 )\n\n")
    # -t arg ( Concurrent number run. default set to ( 20 ) eg. -t 100 )
    tl_com.add_argument("-t",default=20,type=int,dest="thread",help="\nNUMBER OF THREADS ( DEFAULT: 20 )\n\n\n")
    # -config arg ( Run the tool with the config file. eg. -config conf.ini )
    tl_com.add_argument("-config",dest="configfile",help="CONFIG FILE eg. -config config.ini")
    # -header arg ( Manually set the headers. default ( User-Agent,Accept-Language,Accept-Encodin,Accept,Referer ) eg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us" )
    hp_com.add_argument("-header",type=str,help='HTTP HEADERS ( PLEASE PUT THEM IN DOUBLE QUOTES or QUOTES AND SPLIT THEM WITH PIPE | )\neg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us"\n\n')
    # -hm arg ( Set the request http method. default ( get ) -eg -hm head )
    hp_com.add_argument("-hm",metavar="HTTP VERB",dest="httpmethod",help="\nSET HTTP VERB eg. -hm head ( DEFAULT: GET )\n\n")
    # -timeout arg ( Specify the timeout between requests and threads. default ( 3 ) eg. -timeout 10 )
    hp_com.add_argument("-timeout",default=10,type=int,help='\nHTTP request timeout in seconds eg. -timeout 5 ( DEFAULT: 10 )')
    # -cl arg ( Filter the length of the response content. default ( 0 ) eg. -cl 500 )
    fl_com.add_argument("-cl",metavar="FILTER RESPONSE LENGTH",default=0,dest="filterlength",type=int,help="FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )\n\n")
    # -fs arg ( Filter the response status code default ( None ) eg. -fs 404,403,401 )
    fl_com.add_argument("-fs",metavar="FILTER STATUS CODE",dest="filterstatus",help="FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )")
    # -o arg ( Save result. eg. -o out.txt )
    op_com.add_argument("-o",metavar="TXT OUTPUT",default=False,dest="out",help=f"SAVE THE RESULTS ( ONLY FOUND SUBDOMAIN ) eg. -o res.txt ( ONLY TXT FILES )\n\n")
    # od arg ( Save results in raw format with details eg. -od out.txt )
    op_com.add_argument("-od",metavar="TXT OUTPUT WITH DETAILS",default=False,dest="det",help=f"SAVE THE RESULTS WITH DETAILS ( IP,ASN ...) eg. -od res.txt ( ONLY TXT FILES )\n\n")
    # -oj arg ( Save result in json format. eg. -oj out.txt )
    op_com.add_argument("-oj",metavar="JSON OUTPUT WITH DETAILS",default=False,dest="json",help=f"SAVE THE RESULTS IN JSON FORMAT WITH DETAILS eg. -oj res.json\n\n")
    # -nc arg ( Don't colorize the terminal. default ( False ) eg. -nc )
    op_com.add_argument("-nc",default=False,dest="color",action="store_true",help="DON'T COLORIZE OUTPUT ( DEFAULT: False )\n\n")
    # -silent arg ( Just print the found urls. default ( False ) eg. -silent )
    op_com.add_argument("-silent",default=False,action="store_true",help="ONLY SHOW'S THE RESULTS ( DEFAULT: False )")

    # -h arg ( Shows the above options. )
    hl.add_argument("-h","--help",action='help')

    # Show help message when there is no arguments or there is only -h or --help argument.
    if len(sys.argv) == 2 or "-h" in sys.argv or "--help" in sys.argv:
        parser.print_help(sys.stderr)
        exit(f"\n{Fore.LIGHTRED_EX}EXAMPLE USAGE\n\n\t{Fore.YELLOW}DEFAULT ( IT EMPLOYS THE TOOL CONFIGURATION ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py active -u https://ZEE.domain.com\n\n\t{Fore.YELLOW}CONFIG FILE ( YOU CAN SPECIFY YOUR OWN CONFIG FILE ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py active -u https://ZEE.domain.com -config config_file.ini\n\n\t{Fore.YELLOW}ENUMERATE SUBDOMAINS FROM WORDLIST WITH 100 THREADS AND 5 SECONDS TIMEOUT\n\tDON'T COLORIZE THE OUTPUT ( YOU CAN CHANGE THE AMOUNT OF ARGUMANTS ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py active -u https://ZEE.domain.com -w subdomains.txt -t 100 -timeout 5 -nc")
    
    # user arguments
    opts = (parser.parse_known_args())

    # # if there is unknown argument check then show the error message
    if opts[1][-1]:
        if opts[1][-1].lower() == "active" or opts[1][-1].lower() == "passive":
           # return the user args if the unknown args was active or passive
            return opts
        else:
            # else show the error message
            print(f"\n{Fore.RED}[ERROR] UNKNOWN ARGUMENT",end=" ")
            for ex_wrong_args in opts[1]:
                if ex_wrong_args.lower() == "active" or ex_wrong_args.lower() == "passive":
                    pass
                else:
                    print(f"{Fore.WHITE}{ex_wrong_args}",end=" ")
            exit("\n")


def get_passive_args():
    # set main parser
    parser = argparse.ArgumentParser(usage=SUPPRESS,formatter_class=RawTextHelpFormatter,exit_on_error=False,add_help=False,description=Fore.CYAN+f"")
    parser._action_groups.pop()

    hl = parser.add_argument_group("HELP")
    tl_com = parser.add_argument_group('PASSIVE OPTIONS')
    hp_com = parser.add_argument_group('CHECK LIVE')
    op_com = parser.add_argument_group('OUTPUT')

    # -u arg ( Specify the target url for subdomain enumeration. ) eg. -u https://zee.domain.com
    tl_com.add_argument("-u",metavar='TARGET',type=str,dest="URL",help="TARGET URL eg. -u domain.com\n\n")
    # -ul arg ( Specify the url list for subdomain enumeration. ) eg. -ul urls.txt
    tl_com.add_argument("-ul",metavar='LIST OF URLS',type=str,dest="URL_LIST",help="\nURL LIST eg. -ul urls.txt\n\n")
    # -t arg ( Concurrent number run. default set to ( 3 ) eg. -t 10 )
    tl_com.add_argument("-t",type=int,dest="thread",help="\nNUMBER OF THREADS ( DEFAULT: 20 )\n\n")
    # -config arg ( Run the tool with the config file. eg. -config conf.ini )
    tl_com.add_argument("-config",dest="configfile",help="\nCONFIG FILE eg. -config config.ini")
    # -check arg ( Check for live subdomains. default ( False )
    hp_com.add_argument("-check",dest="check_live",action="store_true",help='CHECK FOR LIVE SUBDOMAINS eg. -check ( DEFAULT: False )\n\n')
    # -cl arg ( Filter the length of the response content. default ( 0 ) eg. -cl 500 )
    hp_com.add_argument("-cl",metavar="FILTER RESPONSE LENGTH",dest='filterlength',type=int,help="FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )\n\n")
    # -fs arg ( Filter the response status code.. default ( None ) eg. -fs 404,403,401 )
    hp_com.add_argument("-fs",metavar="FILTER STATUS CODE",dest="filterstatus",help="FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )")
    # or arg ( Save results raw eg. -or out.txt )
    op_com.add_argument("-o",metavar="TXT OUTPUT",default=False,dest="raw",help=f"SAVE THE RESULTS eg. -o res.txt ( ONLY TXT FILES )")
    # -oj arg ( Save result in json format. eg. -oj out.txt )
    op_com.add_argument("-oj",metavar="JSON OUTPUT",default=False,dest="json",help=f"SAVE THE RESULTS IN JSON FORMAT eg. -oj res.json")
    # -nc arg ( Don't colorize the terminal. default ( False ) eg. -nc )
    op_com.add_argument("-nc",default=False,dest="color",action="store_true",help="DON'T COLORIZE OUTPUT ( DEFAULT: False )")
    # -v arg ( USE THE TOOL WITH DETAILS. default ( False ) eg. -v)
    op_com.add_argument("-v",default=False,dest="verb",action="store_true",help="VERBOSE MODE ( DEFAULT: False )")
    # -silent arg ( Just print the found urls. default ( False ) eg. -silent )
    op_com.add_argument("-silent",default=False,action="store_true",help="ONLY SHOW'S THE RESULTS ( DEFAULT: False )")

    # -h arg ( Shows the above options. )
    hl.add_argument("-h","--help",action='help')

    # Show help message when there is no arguments or there is only -h or --help argument.
    if len(sys.argv) == 2 or "-h" in sys.argv or "--help" in sys.argv:
        parser.print_help(sys.stderr)
        exit(f"\n{Fore.LIGHTRED_EX}EXAMPLE USAGE\n\n\t{Fore.YELLOW}SIMPLE ( IT EMPLOYS THE TOOL CONFIGURATION )\n\t\t{Fore.LIGHTGREEN_EX}python zee.py passive -u domain.com\n\n\t{Fore.YELLOW}CONFIG FILE ( YOU CAN SPECIFY YOUR OWN CONFIG FILE )\n\t\t{Fore.LIGHTGREEN_EX}python zee.py passive -u domain.com -config conf.ini\n\n\t{Fore.YELLOW}RUN TOOL FASTER WITH -t ARGUMENT\n\tALSO, YOU CAN SPECIFY A LIST OF DOMAINS WITH THE -ul ARGUMENT\n\t\t{Fore.LIGHTGREEN_EX}python zee.py passive -uL urls.txt -t 5\n\n\t{Fore.YELLOW}YOU CAN RUN THE TOOL SILENTLY WITH -silent ARGUMENT AND ONLY GET THE RESULTS\n\t\t{Fore.LIGHTGREEN_EX}python zee.py passive -ul urls.txt -silent\n\n\t{Fore.YELLOW}WITH -check YOU FILTER THE RESULTS -check WILL CHECK FOR LIVE SUBDOMAINS\n\tALSO YOU CAN FILTER THE -check RESULTS TOO.\n\tFOR EXAMPLE WITH -fs YOU CAN FILTER THE LIVE SUBDOMAINS STATUS CODES\n\tWITH -cl YOU CAN FILTER THE LIVE PAGE CONTENT LENGTH\n\t"+f'\t{Fore.LIGHTGREEN_EX}python zee.py passive -u domain.com -check -fs 404,403,401 -cl 500')
    
    # user arguments
    opts = (parser.parse_known_args())

    # # if there is unknown argument check then show the error message
    if opts[1][-1]:
        if opts[1][-1].lower() == "active" or opts[1][-1].lower() == "passive":
           # return the user args if the unknown args was active or passive
            return opts
        else:
            # else show the error message
            print(f"\n{Fore.RED}[ERROR] UNKNOWN ARGUMENT",end=" ")
            for ex_wrong_args in opts[1]:
                if ex_wrong_args.lower() == "active" or ex_wrong_args.lower() == "passive":
                    pass
                else:
                    print(f"{Fore.WHITE}{ex_wrong_args}",end=" ")
            exit("\n")