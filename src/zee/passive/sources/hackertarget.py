__all__ = ['run_hackertarget']
import requests
from bs4 import BeautifulSoup

def run_hackertarget(*args):

    TARGET = args[0]
    res = []
    def ex_data(data):
        if len(data) > 0:
            spl = str(data).split("\n")
            
            for ex_subdomains in spl:
                split_domain = ex_subdomains.split(",")[0]
                if len(split_domain) > 1 and not split_domain in res:
                    if str(split_domain).lower().endswith(str(TARGET).lower()):
                        if not split_domain == TARGET:
                            res.append(str(split_domain))

    try:

        hackertarget_req = requests.get(f"https://api.hackertarget.com/hostsearch/?q={TARGET}").text
        ex_data(hackertarget_req)

    except:
        return ["hackertarget",[]]
    
    return ["hackertarget",res]