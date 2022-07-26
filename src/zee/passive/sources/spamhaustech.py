__all__ = ['run_spamhaustech']
import json,requests,re

def run_spamhaustech(*args):

    TARGET = args[0]
    username = args[1]['spamhaustech_username']
    password = args[1]['spamhaustech_password']
    if not username:
        return ['spamhaustech',"USERNAME IS NOT SPECIFIED","ERROR"]
    if not password:
        return ['spamhaustech',"PASSWORD IS NOT SPECIFIED","ERROR"]

    res = []

    def ex_subs(domain):
        def check_ip(ip):
            return re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip)

        if check_ip(domain):
            pass
        else:
            if not str(domain) == TARGET:
                if not str(domain) in res and str(domain).lower().endswith(str(TARGET).lower()):
                    res.append(str(domain))


    def ex_data(data):
        for ex_json in data:
            ex_subs(ex_json['rdata'])
            ex_subs(ex_json['rrname'])



    def main(bearer_token):

        head = {"Content-Type": "application/json","Authorization":f"Bearer {bearer_token}"}
        spamhaustech_req  =  requests.get(f"https://api-pdns.spamhaustech.com/v2/_search/rrset/{TARGET}/ANY?stype=rm&limit=1000",headers=head)
        
        if spamhaustech_req.status_code == 200:
            json_res = json.loads(spamhaustech_req.text)
        
            if len(json_res['records']) > 0:
                ex_data(json_res['records'])

            else:
                return ["spamhaustech",res]
        
        else:
            return ["spamhaustech",str(spamhaustech_req.status_code),"ERROR"]
        

    data = json.dumps({"username":username, "password":password})
    token_req = requests.post("https://api-pdns.spamhaustech.com/v2/login",headers={"Content-Type": "application/json", "Accept": "application/json"},data=data)
    
    if token_req.status_code == 401:
        return ['spamhaustech',"INVALID CREDENTIALS ( 401 )","ERROR"]

    elif token_req.status_code == 403:
        return ['spamhaustech',"UNAUTHORIZED ( 403 )","ERROR"]
    
    elif token_req.status_code == 429:
        return ['spamhaustech',"RATE LIMITED ( 429 )","ERROR"]
    
    elif token_req.status_code == 200:
        main(json.loads(token_req.text)['token'])
    
    else:
        return ["spamhaustech",str(token_req.status_code),"ERROR"]


    return ["spamhaustech",res]