__all__ = ['run_asksearch']
import requests,tldextract
from bs4 import BeautifulSoup

def run_asksearch(*args):

    TARGET = args[0]
    res = []

    def ex_data(data):
        soup = BeautifulSoup(data, "html.parser")
        ex_links = soup.find_all(class_="result-link")
        if len(ex_links):
            for ex in ex_links:

                url = ex.get("href")
                domain_name = tldextract.extract(url).domain
                full_domain = tldextract.extract(url).subdomain+"."+domain_name+"."+tldextract.extract(url).suffix
                if tldextract.extract(TARGET).domain ==  domain_name and  not full_domain in res:
                    res.append(full_domain)
    try:
        ask_req = requests.get(f"https://www.ask.com/web?o=0&l=dir&ad=dirN&q=site:*.{TARGET}+-www").text
        ex_data(ask_req)
    except:
        try:
            import time;time.sleep(3)
            ask_req = requests.get(f"https://www.ask.com/web?o=0&l=dir&ad=dirN&q=site:*.{TARGET}+-www").text
            ex_data(ask_req)
        except Exception as er:
            return ["asksearch",er,"ERROR"]

    return ["asksearch",res]