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

        payload = {"UrlBox" : f"https://api.hackertarget.com/hostsearch/?q={TARGET}","AgentList" : "Google Chrome","MethodList" : "GET"}
        hackertarget_req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx" , payload).text
        
        soup = BeautifulSoup(hackertarget_req,"html.parser") 
        soup_text = soup.find("div" ,  id="ResultData").text
        soup_res = soup_text.replace("Response Content","")
        
        ex_data(soup_res)

    except:
        return ["hackertarget",[]]
    
    return ["hackertarget",res]