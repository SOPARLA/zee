__all__ = ['run_censys']
import json,requests

def run_censys(*args):

    TARGET = args[0]
    id = args[1]['censys_api']
    secret = args[1]['censys_pas']
    if not id:
        return ['censys',"ID IS NOT SPECIFIED","ERROR"]
    if not secret:
        return ['censys',"SECRET IS NOT SPECIFIED","ERROR"]

    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com","Content-Type": "application/json", "Accept": "application/json"}
    res = []

    def ex_data(data):
        
        try:
            for ex_subs in data:
                
                for parsed_names in ex_subs['parsed.names']:
                    if not parsed_names in res and str(parsed_names).lower().endswith(str(TARGET).lower()):
                        if not parsed_names == TARGET:
                            res.append(str(parsed_names).rstrip())
                
                for parsed_extensions in ex_subs['parsed.extensions.subject_alt_name.dns_names']:
                    if not parsed_extensions in res and str(parsed_extensions).lower().endswith(str(TARGET).lower()):
                        if not parsed_extensions == TARGET:
                            res.append(str(parsed_extensions).rstrip())
        
        except Exception as err:
            return ['censys',err,"ERROR"]
        
    for p in range(1,1000):
        data = json.dumps({ "query": TARGET, "page": p, "fields": ["parsed.names","parsed.extensions.subject_alt_name.dns_names"], "flatten": True })
        censys_req = requests.post("https://search.censys.io/api/v1/search/certificates",headers=head,data=data,auth=(id,secret))

        
        if censys_req.status_code == 401:
            return ['censys',"INVALID API KEY ( 401 )","ERROR"]

        elif censys_req.status_code == 403:
            return ['censys',"UNAUTHORIZED ( 403 )","ERROR"]
        
        elif censys_req.status_code == 429:
            return ['censys',"RATE LIMITED ( 429 )","ERROR"]
        
        elif censys_req.status_code == 200:
            r = json.loads(censys_req.text)['results']
            if len(r) > 0:
                ex_data(r)
            else:
                break
        
        else:
            return ["censys",str(censys_req.text),"ERROR"]


    return ["censys",res]