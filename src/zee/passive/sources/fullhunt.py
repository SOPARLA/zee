__all__ = ['run_fullhunt']
import json,requests

def run_fullhunt(*args):

    TARGET = args[0]
    key = args[1]['fullhunt']
    if not key:
        return ['fullhunt',"API KEY IS NOT SPECIFIED","ERROR"]

    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com","X-API-KEY":key}
    res = []

    def ex_data(data):
        for ex_subs in data:
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(str(ex_subs).rstrip())


    fullhunt_req = requests.get(f"https://fullhunt.io/api/v1/domain/{TARGET}/subdomains",headers=head)
    

    if fullhunt_req.status_code == 401:
        return ['fullhunt',"INVALID API KEY ( 401 )","ERROR"]

    elif fullhunt_req.status_code == 403:
        return ['fullhunt',"FORBIDDEN ( 403 )","ERROR"]
    
    elif fullhunt_req.status_code == 429:
        return ['fullhunt',"RATE LIMITED ( 429 )","ERROR"]
    
    elif fullhunt_req.status_code == 200:
        ex_data(json.loads(fullhunt_req.text)['hosts'])
    
    else:
        return ["fullhunt",str(fullhunt_req.text),"ERROR"]


    return ["fullhunt",res]