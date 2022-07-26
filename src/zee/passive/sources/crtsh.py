__all__ = ['run_crtsh']
import requests,json

def run_crtsh(*args):
    
    global res
    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    def ex(data):
        ex_json = json.loads(data)
        for ex_subs in ex_json:
            if "\n" in str(ex_subs['name_value']):
                for add in str(ex_subs['name_value']).split("\n"):
                    if not str(add) == TARGET:
                        if not str(add) in res:
                            if not str(add).startswith("*."):
                                if str(add).lower().endswith(str(TARGET).lower()):
                                    res.append(str(add))
            else:    
                if not str(ex_subs['name_value']) == TARGET:
                    if not str(ex_subs['name_value']) in res:
                        if not str(ex_subs['name_value']).startswith("*."):
                            if str(ex_subs['name_value']).lower().endswith(str(TARGET).lower()):
                                res.append(str(ex_subs['name_value']))

            if not str(ex_subs['common_name']) == TARGET:
                if not str(ex_subs['common_name']) in res:
                    if not str(ex_subs['common_name']).startswith("*."):
                        if str(ex_subs['common_name']).lower().endswith(str(TARGET).lower()):
                            res.append(str(ex_subs['common_name']))

    try:
        crt_req = requests.get(f"https://crt.sh/?q=%.{TARGET}&output=json",headers=head)

        if crt_req.status_code == 200:
            if not crt_req == None or not crt_req == "":
                    ex(crt_req.text)
            else:
                return ['crtsh',crt_req.text,"ERROR"]

    except Exception as er:
        try:
        
            import time;time.sleep(3)
            crt_req = requests.get(f"https://crt.sh/?q=%.{TARGET}&output=json",headers=head)
            
            if crt_req.status_code == 200:
                if not crt_req == None or not crt_req == "":
                        ex(crt_req.text)

            else:
                return ['crtsh',crt_req.text,"ERROR"]
        
        except:
            return ['crtsh',er,"ERROR"]
    
    return ['crtsh',res]