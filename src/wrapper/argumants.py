# In this section, we set the args

# Importing the needed libraries
# argparse for set the needed arguments
# colorama library for text coloring
import argparse,sys
from argparse import SUPPRESS
from argparse import RawTextHelpFormatter
from colorama import Fore

def get_args():
    # set main parser
    parser = argparse.ArgumentParser(usage=SUPPRESS,formatter_class=RawTextHelpFormatter,exit_on_error=False,add_help=False,description=Fore.CYAN+f"")
    parser._action_groups.pop()

    hl = parser.add_argument_group("HELP")
    tl_com = parser.add_argument_group('ZEE OPTIONS')
    hp_com = parser.add_argument_group('HTTP OPTIONS')
    fl_com = parser.add_argument_group('FILTER')
    op_com = parser.add_argument_group('OUTPUT')

    # -u arg ( Specify the target url for subdomain enumeration. ) eg. -u https://zee.domain.com
    tl_com.add_argument("-u",type=str,dest="URL",help="TARGET URL eg. -u https://ZEE.domain.com/ | https://ZEE.subdomain.domain.com/\n( PLEASE PUT ZEE IN THE PART THAT YOU WANT TO BRUTE FORCE )\n\n")
    # -w arg ( Specify the wordlist for subdomain enumeration. default set to ( seclist-20000 ) ) eg. -w subdomains.txt
    tl_com.add_argument("-w",dest="wordlist",default="def",help="WORDLIST PATH eg. -w path/subdomains.txt ( DEFAULT: SECLIST-20000 )")
    # -t arg ( Concurrent number run. default set to ( 20 ) eg. -t 100 )
    tl_com.add_argument("-t",default=20,type=int,dest="thread",help="NUMBER OF THREADS ( DEFAULT: 20 )")
    # -config arg ( Run the tool with the config file. eg. -config conf.ini )
    tl_com.add_argument("-config",dest="configfile",help="CONFIG FILE eg. -config config.ini")
    # -v arg ( Shows the tool version in terminal. eg. -v )
    tl_com.add_argument("-v",action='store_true',dest="toolversion",help="TOOL VERSION")
    # -header arg ( Manually set the headers. default ( User-Agent,Accept-Language,Accept-Encodin,Accept,Referer ) eg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us" )
    hp_com.add_argument("-header",type=str,help='HTTP HEADERS ( PLEASE PUT THEM IN DOUBLE QUOTES or QUOTES AND SPLIT THEM WITH PIPE | )\neg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us"\n\n')
    # -hm arg ( Set the request http method. default ( get ) -eg -hm head )
    hp_com.add_argument("-hm",dest="httpmethod",help="SET HTTP METHOD eg. -hm head ( DEFAULT: GET )")
    # -timeout arg ( Specify the timeout between requests and threads. default ( 3 ) eg. -timeout 10 )
    hp_com.add_argument("-timeout",default=3,type=int,help='HTTP request timeout in seconds eg. -timeout 5 ( DEFAULT: 3 )')
    # -cl arg ( Filter the length of the response content. default ( 0 ) eg. -cl 500 )
    fl_com.add_argument("-cl",default=0,dest="filterlength",type=int,help="FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )")
    # -cl arg ( Filter the response status code.. default ( None ) eg. -fs 404,403,401 )
    fl_com.add_argument("-fs",dest="filterstatus",help="FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )")
    # -os arg ( Save only the urls in specified file. eg. -os out.txt )
    op_com.add_argument("-os",default=False,dest="simple_save",help=f"SAVE RESULTS SIMPLE OUTPUT eg. -os res.txt ( ONLY TXT FILES )")
    # -od arg ( Save result with ip and asn in specified file. eg. -od out.txt )
    op_com.add_argument("-od",default=False,dest="advanced_save",help=f"SAVE THE RESULTS ADVANCED OUTPUT eg. -od res.txt ( ONLY TXT FILES )")
    # -nc arg ( Don't colorize the terminal. default ( False ) eg. -nc )
    op_com.add_argument("-nc",default=False,dest="color",action="store_true",help="DON'T COLORIZE OUTPUT ( DEFAULT: False )")
    # -silent arg ( Just print the found urls. default ( False ) eg. -silent )
    op_com.add_argument("-silent",default=False,action="store_true",help="ONLY SHOW'S THE RESULTS ( DEFAULT: False )")

    # -h arg ( Shows the above options. )
    hl.add_argument("-h","--help",action='help')

    # Show help message when there is no arguments or there is only -h or --help argument.
    if len(sys.argv)<= 1 or "-h" in sys.argv or "--help" in sys.argv:
        parser.print_help(sys.stderr)
        sys.exit(f"\n{Fore.LIGHTRED_EX}EXAMPLE USAGE\n\n\t{Fore.YELLOW}DEFAULT ( IT EMPLOYS THE TOOL CONFIGURATION FILE DEFAULT ARGUMENT ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py -u https://ZEE.domain.com\n\n\t{Fore.YELLOW}CONFIG FILE ( YOU CAN SPECIFY YOUR OWN CONFIG FILE ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py -u https://ZEE.domain.com -config config_file.ini\n\n\t{Fore.YELLOW}ENUMRATE SUBDOMAINS FROM WORDLIST WITH 100 THREADS AND 5 SECONDS TIMEOUT\n\tDON'T COLORIZE THE OUTPUT ( YOU CAN CHANGE THE AMOUNT OF ARGUMANTS ).\n\t\t{Fore.LIGHTGREEN_EX}python zee.py -u https://ZEE.domain.com -w subdomains.txt -t 100 -timeout 5 -nc\n\n\t{Fore.YELLOW}FILTER RESPONSE STATUS CODES 404,403,401 WITH -fs OPTION, FILTER RESPONSE PAGE LENGTH TILL 500 WITH -cl OPTION\n\tSEND REQUESTS WITH THE HEAD HTTP METHOD WITH -hm OPTION, SETTING THE REQUEST HEADERS WITH -header\n\t( YOU CAN CHANGE THE AMOUNT OF ARGUMANTS ).\n\t"+f'{Fore.LIGHTGREEN_EX}python zee.py -u https://zee.domain.com -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us"')
    
    # user arguments
    opts = (parser.parse_known_args())
    # if there is unknown argument show the error message
    if opts[1]:
        sys.exit(Fore.RED+f"\n[ERROR] WRONG ARGUMENT {opts[1][0]}\n")
    # else return the user args
    else:
        return opts