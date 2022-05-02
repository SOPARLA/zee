from colorama import Fore
from tldextract import extract

def banner():
    print()
    print(Fore.LIGHTMAGENTA_EX+r"""__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_        
 _\////////////\\\__\/\\\///////////__\/\\\///////////__       
  ___________/\\\/___\/\\\_____________\/\\\_____________      
   _________/\\\/_____\/\\\\\\\\\\\_____\/\\\\\\\\\\\_____     
    _______/\\\/_______\/\\\///////______\/\\\///////______    
     _____/\\\/_________\/\\\_____________\/\\\_____________   
      ___/\\\/___________\/\\\_____________\/\\\_____________  
       __/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_ 
        _\///////////////__\///////////////__\///////////////__"""+f"\n\n\t\t{Fore.RED}Version 1.0 ")
   

def ncbanner():
    print()
    print(r"""__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_        
 _\////////////\\\__\/\\\///////////__\/\\\///////////__       
  ___________/\\\/___\/\\\_____________\/\\\_____________      
   _________/\\\/_____\/\\\\\\\\\\\_____\/\\\\\\\\\\\_____     
    _______/\\\/_______\/\\\///////______\/\\\///////______    
     _____/\\\/_________\/\\\_____________\/\\\_____________   
      ___/\\\/___________\/\\\_____________\/\\\_____________  
       __/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_ 
        _\///////////////__\///////////////__\///////////////__"""+f"\n\n\t\tVersion 1.0 ")
def main(TARGET,wordlist,wordlist_len,http_method,status_code,tout,length,thread_count,dont_colorize):
    ex = extract(TARGET)
    TARGET = f"{ex.domain}.{ex.suffix}"
    if dont_colorize:
        ncbanner()
        print(f"\n   [*] TARGET\t\t : {TARGET}\n   [*] THREADS\t\t : {thread_count}\n   [*] TIMEOUT\t\t : {tout}\n   [*] WORDLIST\t\t : {wordlist}\n   [*] SUBDOMAINS\t : {wordlist_len}\n   [*] FILTERD CODES\t : {status_code}\n   [*] FILTERD LENGTH\t : {length}\n   [*] REQUEST METHOD\t : {http_method}\n\n")
    else:
        banner()
        print(f"\n   {Fore.RED}[*] {Fore.CYAN}TARGET\t\t : {TARGET}\n   {Fore.RED}[*] {Fore.CYAN}THREADS\t\t : {thread_count}\n   {Fore.RED}[*] {Fore.CYAN}TIMEOUT\t\t : {tout}\n   {Fore.RED}[*] {Fore.CYAN}WORDLIST\t\t : {wordlist}\n   {Fore.RED}[*] {Fore.CYAN}SUBDOMAINS\t : {wordlist_len}\n   {Fore.RED}[*] {Fore.CYAN}FILTERD CODES\t : {status_code}\n   {Fore.RED}[*] {Fore.CYAN}FILTERD LENGTH\t : {length}\n   {Fore.RED}[*] {Fore.CYAN}REQUEST METHOD\t : {http_method}\n\n")