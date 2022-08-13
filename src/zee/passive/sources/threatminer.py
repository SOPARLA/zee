__all__ = ['run_threatminer']
import json,requests

def run_threatminer(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    threatminer_req = requests.get(f"https://api.threatminer.org/v2/domain.php?q={TARGET}&rt=5",headers=head).text
    ex_json = json.loads(threatminer_req)
    
    if ex_json['status_code'] == "200":
        for ex_subs in ex_json['results']:
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(ex_subs)

    else:
        return ["threatminer",[]]
    
    return ["threatminer",res]