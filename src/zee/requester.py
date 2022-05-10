# socket library for getting the domain ip
# re library for search in html code with regex
import socket,re

try:
    # urllib3 for disable urllib3 warnings 
    import urllib3
except ModuleNotFoundError:
    exit("\033[91m\n[ERROR] MODULE NOT FOUND\nPLEASE INSTALL urllib3 MODULE\n\teg. pip install urllib3\n")

try:
    # bs4 library for search in html code
    from bs4 import BeautifulSoup as B
except ModuleNotFoundError:
    exit("\033[91m\n[ERROR] MODULE NOT FOUND\nPLEASE INSTALL beautifulsoup4 MODULE\n\teg. pip install beautifulsoup4\n")

try:
    # requests library for sending http requests
    import requests
except ModuleNotFoundError:
    exit("\033[91m\n[ERROR] MODULE NOT FOUND\nPLEASE INSTALL requests MODULE\n\teg. pip install requests\n")

disable_warnings = urllib3.disable_warnings()

def send_request(url,header,timeout,http_method):
    try:

        # get ip and asn domain with get_ip_asn function
        def get_ip_asn(data):
            # Replace the http protocol in the URL with None.
            if "https://" in data or "http://" in data:
                data = str(data).replace("https://","").replace("http://","")

            # get domain ip with socket
            ip = socket.gethostbyname(data)

            # search domain asn in tools.iplocation.net/ip-to-asn
            get_asn = requests.post("https://tools.iplocation.net/ip-to-asn",data={"ip":ip,"submit":"Submit"}).text
            soup = B(get_asn,"html.parser")
            find = soup.find("div",{"class":"col col_12_of_12"})
            asn = re.findall("ASN : (.*)",find.text)

            return [ip,asn[0]]

        send_req = requests.request(url=str(url),verify=False,method=http_method,timeout=timeout,headers=header,allow_redirects=False)
        det = get_ip_asn(url)

    except requests.exceptions.ConnectionError:
        return "FAILED"
    except requests.exceptions.InvalidURL:
        return "FAILED"
    except requests.exceptions.ReadTimeout:
        return "FAILED"
    else:
        return [send_req,det[0],det[1]]
