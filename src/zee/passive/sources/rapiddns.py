__all__ = ['run_rapiddns']
import requests;from bs4 import BeautifulSoup

def run_rapiddns(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    rapid_req = requests.get(f"https://rapiddns.io/subdomain/{TARGET}",headers=head).text
    html_text = BeautifulSoup(rapid_req,"html.parser")
    
    for ex_rapid_subs in html_text.find_all("tr"):
        spl_data = (str(ex_rapid_subs.text)).rsplit()
        domain = str(spl_data[1])
        
        if domain == "Domain":
            continue
 
        else:
            if not str(domain) == TARGET:
                if not str(domain) in res and str(domain).lower().endswith(str(TARGET).lower()):
                    res.append(str(domain))

    return ['rapiddns',res]