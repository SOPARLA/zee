__all__ = ['run_binaryedge']
import requests,json

def run_binaryedge(*args):

    TARGET = args[0]
    key = args[1]['binaryedge_api']
    if not key:
        return ['binaryedge',"API KEY IS NOT SPECIFIED","ERROR"]

    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com","X-Key":key}
    res = []

    def ex_data(data):
        for ex_subs  in data:
            if not str(ex_subs) == TARGET:
                if not str(ex_subs) in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                    res.append(str(ex_subs))


    for pages in range(1,1000000):
        param = {'page': pages}

        try:
            binaryedge_req = requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{TARGET}",params=param,headers=head)
            if binaryedge_req.status_code == 401:
                return ['binaryedge',"INVALID API KEY ( 401 )","ERROR"]
        
            elif binaryedge_req.status_code == 403:
                return ['binaryedge',"YOUR SUBSCRIPTION ENDED ( 403 )","ERROR"]
        
            elif binaryedge_req.status_code == 200:
                try:
                    ev = json.loads(binaryedge_req.text)['events']
                    if len(ev) < 1:
                        return ["binaryedge",res]
                    ex_data(ev)
                except:
                    return ["binaryedge",res]
            
            else:
                return ["binaryedge",str(binaryedge_req.text),"ERROR"]
                
        except:

            import time;time.sleep(2)
            binaryedge_req = requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{TARGET}",params=param,headers=head)
            
            if binaryedge_req.status_code == 401:
                return ['binaryedge',"INVALID API KEY ( 401 )","ERROR"]
        
            elif binaryedge_req.status_code == 403:
                return ['binaryedge',"YOUR SUBSCRIPTION ENDED ( 403 )","ERROR"]
        
            elif binaryedge_req.status_code == 200:
                try:
                    ev = json.loads(binaryedge_req.text)['events']
                    if len(ev) < 1:
                        return ["binaryedge",res]
                    ex_data(ev)
                except:
                    return ["binaryedge",res]
            
            else:
                return ["binaryedge",str(binaryedge_req.text),"ERROR"]