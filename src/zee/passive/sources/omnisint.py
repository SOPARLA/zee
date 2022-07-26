__all__ = ['run_omnisint']
import json,requests

def run_omnisint(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    omnisint_req = requests.get(f"https://sonar.omnisint.io/subdomains/{TARGET}",headers=head).text
    ex_json = json.loads(omnisint_req)
    
    if not "error" in ex_json:
        
        for ex_subs in ex_json:
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(ex_subs)

    else:
        return ["omnisint",[]]    
    
    return ["omnisint",res]