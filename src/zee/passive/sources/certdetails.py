__all__ = ['run_certdetails']
from re import I
import requests,tldextract
from bs4 import BeautifulSoup

def run_certdetails(*args):

    TARGET = args[0]
    res = []

    def ex_data(data):
        soup = BeautifulSoup(data, "html.parser")
        ex_links = soup.find_all(class_="columns")

        if len(ex_links):
            for urls in ex_links:
                for last in str(urls.text).split("\n "):
                    if last:
                        domain_name = tldextract.extract(last).domain
                        if tldextract.extract(TARGET).domain == domain_name and not last == TARGET and not last == f"*.{TARGET}" and not last in res:
                            res.append(last)

    try:
        get_location = requests.head(f"https://certificatedetails.com/{TARGET}")
        if not get_location.status_code == 404:
            main_req = requests.get(f"https://certificatedetails.com/{get_location.headers['Location']}/{TARGET}").text
            ex_data(main_req)
    except:
        try:
            import time;time.sleep(3)
            get_location = requests.head(f"https://certificatedetails.com/{TARGET}")
            if not get_location.status_code == 404:
                main_req = requests.get(f"https://certificatedetails.com/{get_location.headers['Location']}/{TARGET}").text
                ex_data(main_req)

        except Exception as er:
            return ["certdetails",er,"ERROR"]

    return ["certdetails",res]