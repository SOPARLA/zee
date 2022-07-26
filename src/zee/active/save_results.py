# json library write results as json.
# tldextract is used to extract the urls section.
import tldextract,json

def save(file_name,results,domain):
    # GET DOMAIN NAME
    domain = tldextract.extract(domain).domain

    spl = str(file_name).split(":")
    
    # WRITE RESULTS IN RAW MODE ( .txt )
    def simple(name,data):
        res_path = open(name,"a")
        for last in data:
            res_path.write(str(last)+"\n")

    # WRIT RESULTS IN JSON MODE ( .json )
    def js(name,data,target_domain):
        main_json = {str(target_domain):{}}
        main_json[target_domain]=data
        with open(name,"a") as res_path:
            res_path.write(json.dumps(main_json))

    # if user used -o write results in raw mode 
    if spl[1] == "simple":
        simple(spl[0],results)
    
    # if user used -od write results in raw mode
    elif spl[1] == "detail":
        simple(spl[0],results)
    
    # if user used -oj write results in json mode
    elif spl[1] == "json":
        js(spl[0],results,domain)
    
    else:
        pass