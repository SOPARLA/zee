__all__ = ['run_securitytrails']
import json,requests

def run_securitytrails(*args):

    TARGET = args[0]
    key = args[1]['securitytrails']
    if not key:
        return ['securitytrails',"API KEY IS NOT SPECIFIED","ERROR"]
    
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com","APIKEY":key}
    res = []

    def ex_data(data):
        for ex_subs in data:
            ex_subs = f"{ex_subs}.{TARGET}"
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(str(ex_subs).rstrip())

    securitytrails_req = requests.get(f"https://api.securitytrails.com/v1/domain/{TARGET}/subdomains",headers=head)
    
    if securitytrails_req.status_code == 401:
        return ['securitytrails',"INVALID API KEY ( 401 )","ERROR"]

    elif securitytrails_req.status_code == 403:
        return ['securitytrails',"FORBIDDEN ( 403 )","ERROR"]
    
    elif securitytrails_req.status_code == 429:
        return ['securitytrails',"RATE LIMITED ( 429 )","ERROR"]
    
    elif securitytrails_req.status_code == 200:
        ex_data(json.loads(securitytrails_req.text)['subdomains'])
    
    else:
        return ["securitytrails",str(securitytrails_req.text),"ERROR"]

    return ["securitytrails",res]