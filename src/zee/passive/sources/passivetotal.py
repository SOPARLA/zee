__all__ = ['run_passivetotal']
import json,requests

def run_passivetotal(*args):

    TARGET = args[0]
    username = args[1]['passivetotal_email']
    password = args[1]['passivetotal_pass']
    if not username:
        return ['passivetotal',"USERNAME IS NOT SPECIFIED","ERROR"]
    if not password:
        return ['passivetotal',"PASSWORD IS NOT SPECIFIED","ERROR"]
    
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com","Content-Type": "application/json", "Accept": "application/json"}
    res = []

    def ex_data(data):
        for ex_subs in data:
            ex_subs = f"{ex_subs}.{TARGET}"
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(str(ex_subs).rstrip())


    data = json.dumps({ "query": TARGET})
    passivetotal_req = requests.get(f"https://api.passivetotal.org/v2/enrichment/subdomains",headers=head,data=data,auth=(username,password))
    
    if passivetotal_req.status_code == 401:
        return ['passivetotal',"INVALID CREDENTIALS ( 401 )","ERROR"]

    elif passivetotal_req.status_code == 403:
        return ['passivetotal',"FORBIDDEN ( 403 )","ERROR"]
    
    elif passivetotal_req.status_code == 429:
        return ['passivetotal',"RATE LIMITED ( 429 )","ERROR"]
    
    elif passivetotal_req.status_code == 200:
        ex_data(json.loads(passivetotal_req.text)['subdomains'])
    
    else:
        return ["passivetotal",str(passivetotal_req.text),"ERROR"]

    return ["passivetotal",res]