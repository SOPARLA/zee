import urllib3,requests,socket,re
from bs4 import BeautifulSoup as B

disable_warnings = urllib3.disable_warnings()
def send_request(url,header,timeout,http_method):
    try:
        
        def get_ip_asn(data):
            if "https://" in data or "http://" in data:
                data = str(data).replace("https://","").replace("http://","")
            ip = socket.gethostbyname(data)
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
