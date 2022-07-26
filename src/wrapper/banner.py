# colorama library for colorize terminal.
from colorama import Fore


# help banner
def help_banner():
    banner()
    print(Fore.CYAN+"""\nZEE MAIN ARGS:\n\tactive\t\tACTIVE  SUBDOMAIN SCAN\n\tpassive\t\tPASSIVE SUBDOMAIN SCAN\n\tversion\t\tCHECK FOR NEW VERSION""")

# GET CURRENT TOOL VERSION FROM VERSION.TXT FILE
with open("src/general/version.txt","r") as ver:
    ver = ver.read()

# print the banner with magenta color
def banner():
    print("\n"+Fore.LIGHTMAGENTA_EX+r"""__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_        
 _\////////////\\\__\/\\\///////////__\/\\\///////////__       
  ___________/\\\/___\/\\\_____________\/\\\_____________      
   _________/\\\/_____\/\\\\\\\\\\\_____\/\\\\\\\\\\\_____     
    _______/\\\/_______\/\\\///////______\/\\\///////______    
     _____/\\\/_________\/\\\_____________\/\\\_____________   
      ___/\\\/___________\/\\\_____________\/\\\_____________  
       __/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_ 
        _\///////////////__\///////////////__\///////////////__"""+f"\n\n\t\t{Fore.RED}Version {ver}")
   
# print the banner with out color
def ncbanner():
    print("\n"+r"""__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_        
 _\////////////\\\__\/\\\///////////__\/\\\///////////__       
  ___________/\\\/___\/\\\_____________\/\\\_____________      
   _________/\\\/_____\/\\\\\\\\\\\_____\/\\\\\\\\\\\_____     
    _______/\\\/_______\/\\\///////______\/\\\///////______    
     _____/\\\/_________\/\\\_____________\/\\\_____________   
      ___/\\\/___________\/\\\_____________\/\\\_____________  
       __/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_ 
        _\///////////////__\///////////////__\///////////////__"""+f"\n\n\t\tVersion {ver} ")


def active_banner(TARGET,wordlist,wordlist_len,http_method,status_code,tout,length,thread_count,dont_colorize):
    
    # If the wordlist was the tool's default wordlist, set the wordlist name in banner seclist-20000.txt.
    if wordlist == "def":
        wordlist = "seclist-20000.txt"
    
    # If -nc was used, it would run the no-color banner with information.
    if dont_colorize:
        ncbanner()
        print(f"\n   [*] TARGET\t\t : {TARGET}\n   [*] THREADS\t\t : {thread_count}\n   [*] TIMEOUT\t\t : {tout}\n   [*] WORDLIST\t\t : {wordlist}  {wordlist_len}\n   [*] FILTERD CODES\t : {status_code}\n   [*] FILTERD LENGTH\t : {length}\n   [*] REQUEST METHOD\t : {http_method}\n\n")
    
    # Or run the colorized banner with information.
    else:
        banner()
        print(f"\n   {Fore.RED}[*] {Fore.CYAN}TARGET\t\t : {TARGET}\n   {Fore.RED}[*] {Fore.CYAN}THREADS\t\t : {thread_count}\n   {Fore.RED}[*] {Fore.CYAN}TIMEOUT\t\t : {tout}\n   {Fore.RED}[*] {Fore.CYAN}WORDLIST\t\t : {wordlist}  {wordlist_len}\n   {Fore.RED}[*] {Fore.CYAN}FILTERD CODES\t : {status_code}\n   {Fore.RED}[*] {Fore.CYAN}FILTERD LENGTH\t : {length}\n   {Fore.RED}[*] {Fore.CYAN}REQUEST METHOD\t : {http_method}\n\n")

def passive_banner(url,urls,url_length,status_code,length,thread_count,dont_colorize):
    
    if urls:
        # If -nc was used, it would run the no-color banner with information.
        if dont_colorize:
            ncbanner()
            set_ = f"\n   [*]  DOMAINS\t\t : {urls}  {url_length}\n   [*]  THREADS\t\t : {thread_count}" 
            if status_code:
                set_ += f"\n   [*]  FILTERD CODES\t : {status_code}"
            if length:
                set_ += f'\n   [*]  FILTERD LENGTH\t : {length}'
            set_ += "\n\n"
            print(set_)
        
        # Or run the colorized banner with information.
        else:
            banner()
            set_ = f"\n   {Fore.RED}[*] {Fore.CYAN} DOMAINS\t\t : {urls}  {url_length}\n   {Fore.RED}[*] {Fore.CYAN} THREADS\t\t : {thread_count}" 
            if status_code:
                set_ += f"\n   {Fore.RED}[*] {Fore.CYAN} FILTERD CODES\t : {status_code}"
            if length:
                set_ += f'\n   {Fore.RED}[*] {Fore.CYAN} FILTERD LENGTH\t : {length}'
            set_ += "\n\n"
            print(set_)

    else:
        # If -nc was used, it would run the no-color banner with information.
        if dont_colorize:
            ncbanner()
            set_ = f"\n   [*]  TARGET\t\t : {url}\n   [*]  THREADS\t\t : {thread_count}"
            if status_code:
                set_ += f"\n   [*]  FILTERD CODES\t : {status_code}"
            if length:
                set_ += f'\n   [*]  FILTERD LENGTH\t : {length}'
            set_ += "\n\n"
            print(set_)
        
        # Or run the colorized banner with information.
        else:
            banner()
            set_ = f"\n   {Fore.RED}[*]  {Fore.CYAN}TARGET\t\t : {url}\n   {Fore.RED}[*]  {Fore.CYAN}THREADS\t\t : {thread_count}"
            if status_code:
                set_ += f"\n   {Fore.RED}[*] {Fore.CYAN} FILTERD CODES\t : {status_code}"
            if length:
                set_ += f'\n   {Fore.RED}[*] {Fore.CYAN} FILTERD LENGTH\t : {length}'
            set_ += "\n\n"
            print(set_)