__all__ = ['run_alienvault']
import requests,json

def run_alienvault(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    def ex_data(data):
        for ex_otx_subs in data:
            domain = str(ex_otx_subs['hostname']).rstrip()
            if not domain == TARGET:
                if not domain in res and domain.lower().endswith(str(TARGET).lower()):
                    res.append(domain)
    
    def get_subs(domain):
        alienvault_req = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns",headers=head).text
        alienvault_json_content = json.loads(alienvault_req)['passive_dns']
        
        if alienvault_json_content:
            ex_data(alienvault_json_content)
        else:
            return ["alienvault",[]]

    try:
        get_subs(TARGET)
    except json.decoder.JSONDecodeError:
        import time;time.sleep(3)
        get_subs(TARGET)

    return ["alienvault",res]