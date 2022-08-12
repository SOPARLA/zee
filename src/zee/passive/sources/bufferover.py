__all__ = ['run_bufferover']
import requests,json

def run_bufferover(*args):

    TARGET = args[0]
    head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0","Referer":"https://www.google.com"}
    res = []

    def ex_data(data):
        for ex_subs in data:
            subDomain = str(ex_subs.split(",")[1]).rstrip()
            if not subDomain == TARGET:
                if not subDomain in res and subDomain.lower().endswith(str(TARGET).lower()):
                    res.append(subDomain)

    bufferover_req = requests.get(f"https://dns.bufferover.run/dns?q=.{TARGET}",headers=head).text
    fdns = json.loads(bufferover_req)['FDNS_A']
    rdns = json.loads(bufferover_req)['RDNS']

    if not fdns == None:
        ex_data(fdns)

    if not rdns == None:
        ex_data(rdns)

    return ["bufferover",res]