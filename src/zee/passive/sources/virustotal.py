__all__ = ['run_virustotal']
import json,requests

def run_virustotal(*args):

    TARGET = args[0]
    key = args[1]['virustotal']
    if not key:
        return ['virustotal',"API KEY IS NOT SPECIFIED","ERROR"]

    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    def ex_data(data):
        for ex_subs in data:
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(str(ex_subs).rstrip())

    virustotal_req = requests.get(f"https://www.virustotal.com/vtapi/v2/domain/report?apikey={key}&domain={TARGET}",headers=head)
    

    if virustotal_req.status_code == 401:
        return ['virustotal',"INVALID API KEY ( 401 )","ERROR"]

    elif virustotal_req.status_code == 403:
        return ['virustotal',"FORBIDDEN ( 403 )","ERROR"]
    
    elif virustotal_req.status_code == 429:
        return ['virustotal',"RATE LIMITED ( 429 )","ERROR"]
    
    elif virustotal_req.status_code == 200:
        ex_data(json.loads(virustotal_req.text)['subdomains'])
    
    else:
        return ["virustotal",str(virustotal_req.text),"ERROR"]

    return ["virustotal",res]