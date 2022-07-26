__all__ = ['run_certspotter']
import requests,json
from bs4 import BeautifulSoup

def run_certspotter(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    def ex_data(data):
        for ex_subs in data:
            for ex_subs_ in ex_subs['dns_names']:
                if not ex_subs_ == TARGET:
                    if not str(ex_subs_) in res and str(ex_subs_).lower().endswith(str(TARGET).lower()):
                        res.append(str(ex_subs_))
    
    certspotter_req = requests.get(f"https://api.certspotter.com/v1/issuances?domain={TARGET}&include_subdomains=true&expand=dns_names",headers=head).text
    

    if "rate_limited" in certspotter_req:
        payload = {"UrlBox" : f"https://api.certspotter.com/v1/issuances?domain={TARGET}&include_subdomains=true&expand=dns_names","AgentList" : "Google Chrome","MethodList" : "GET"}
        send_new_req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx" , payload).text
        
        soup = BeautifulSoup(send_new_req,"html.parser") 
        soup_text = soup.find("div" ,  id="ResultData").text
        soup_res = soup_text.replace("Response Content","")
        
        if "rate_limited" in soup_res:
            return ['certspotter',"RATE LIMITED","ERROR"]
        else:
            ex_data(json.loads(soup_res))
    
    else:
        ex_data(json.loads(certspotter_req))

    return ['certspotter',res]