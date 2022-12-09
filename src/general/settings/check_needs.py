def start():
    try:
        # colorama library for colorize the terminal
        from colorama import Fore
    except ModuleNotFoundError:
        exit("\033[91m\n[ERROR] MODULE NOT FOUND\n\33[33mPLEASE INSTALL colorama \33[33mMODULE\n\tpip install colorama or pip install -r requirements.txt\n")
    
    try:
        # tldextract is used to extract the urls section.
        import tldextract
    except ModuleNotFoundError:
        exit(f"{Fore.RED}[ERROR] MODULE NOT FOUND\n{Fore.YELLOW}PLEASE INSTALL {Fore.GREEN}tldextract {Fore.YELLOW}MODULE\n\t{Fore.WHITE}pip install tldextract{Fore.RED} or {Fore.WHITE}pip install -r requirements.txt\n")

    try:
        # urllib3 for disable urllib3 warnings 
        import urllib3
    except ModuleNotFoundError:
        exit(f"{Fore.RED}\n[ERROR] MODULE NOT FOUND\n{Fore.YELLOW}PLEASE INSTALL {Fore.GREEN}urllib3 {Fore.YELLOW}MODULE\n\t{Fore.WHITE}pip install urllib3 {Fore.RED}or {Fore.WHITE}pip install -r requirements.txt\n")

    try:
        # bs4 library for search in html code
        from bs4 import BeautifulSoup as B
    except ModuleNotFoundError:
        exit(f"{Fore.RED}\n[ERROR] MODULE NOT FOUND\n{Fore.YELLOW}PLEASE INSTALL {Fore.GREEN}beautifulsoup4 {Fore.YELLOW}MODULE\n\t{Fore.WHITE}pip install beautifulsoup4 {Fore.RED}or {Fore.WHITE}pip install -r requirements.txt\n")
 
    try:
        # requests library for sending http requests
        import requests
    except ModuleNotFoundError:
        exit(f"{Fore.RED}\n[ERROR] MODULE NOT FOUND\n{Fore.YELLOW}PLEASE INSTALL {Fore.GREEN}requests {Fore.YELLOW}MODULE\n\t{Fore.WHITE}pip install requests {Fore.RED}or {Fore.WHITE}pip install -r requirements.txt\n")
    
    try:
        # psycopg2 library for connect to crtsh db
        import psycopg2
    except ModuleNotFoundError:
        exit(f"{Fore.RED}\n[ERROR] MODULE NOT FOUND\n{Fore.YELLOW}PLEASE INSTALL {Fore.GREEN}psycopg2 {Fore.YELLOW}MODULE\n\t{Fore.WHITE}pip install psycopg2 {Fore.RED}or {Fore.WHITE}pip install -r requirements.txt\n")
    
    # check the current python version with platform library
    import platform
    py_version = platform.python_version()
    if py_version.startswith("3"):
        pass
    else:
        exit(Fore.RED+F"\n\n[ERROR] THE PYTHON VERSION DOES NOT MATCH WITH THE REQUIRED VERSION\n\t{Fore.YELLOW}CURRENT VERSION {py_version}\n\t{Fore.LIGHTGREEN_EX}REQUIRED VERSION 3 OR HIGHER\n")