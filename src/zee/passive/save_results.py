# json library write results as json.
# tldextract is used to extract the urls section.
import json,tldextract

def save(file_name,results,domain):

    # GET URL DOMAIN NAME
    domain = tldextract.extract(domain).domain

    # WRITE IN TXT FORMAT
    def write_raw(name,data):
        res_path = open(name,"a")
        for last in data:
            res_path.write(str(last)+"\n")

    # WRITE IN JSON FORMAT
    def write_json(name,data):
        json_data = {domain:{}}
        json_data[domain]=data
        with open(name,"a") as res_path:
            res_path.write(json.dumps(json_data))


    file_name = str(file_name).split(":")
    
    # if user used -o write results in raw mode
    if file_name[1].lower() == "raw":
        write_raw(file_name[0],results)

    # if user used -oj write results in json mode
    elif file_name[1].lower() == "json":
        write_json(file_name[0],results)
