__all__ = ['run_jldc']
import json,requests

def run_jldc(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    jldc_req = requests.get(f"https://jldc.me/anubis/subdomains/{TARGET}",headers=head).text
    ex_json = json.loads(jldc_req)

    if ex_json:
        for ex_subs in ex_json:
            if not ex_subs in res and str(ex_subs).lower().endswith(str(TARGET).lower()):
                if not ex_subs == TARGET:
                    res.append(str(ex_subs).rstrip())
    else:
        return ["jldc",[]]

    return ["jldc",res]