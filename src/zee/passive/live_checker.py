# requests library for send the requests
# urllib3 library to disable the http warnings.
# socket library to get the subdomain IP
# For faster request sending, use the concurrent.futures library
import requests,urllib3,socket
from .print_results import *
from .save_results import  save
from concurrent.futures import ThreadPoolExecutor

def live(urls,fstatus,flength,thread,output,domain):
    global res
    urllib3.disable_warnings()
    failed = []
    results = []

    def main(TARGET):

        def run(domain):
            try:
                head = head = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0" ,"Referer":"https://www.google.com"}
                send_req = requests.get("https://"+domain,verify=False,timeout=5,headers=head)
                
                # SUBDOMAIN IP ADDRESS
                ipaddr = socket.gethostbyname(domain)
                # REQUEST CODE RESPONSE
                req_stcode  = send_req.status_code
                # PAGE CONTENT
                req_content = send_req.content
                # RESPONSE HEADER
                req_headers = send_req.headers

                # CHECK FOR content-length in headers
                # EXTRACTING THE RESPONSE PAGE LENGTH
                if 'content-length' in req_headers:
                    length = req_headers['content-length']
                else:
                    length = len(req_content)
                
                # check if user want to filter the response code
                if fstatus:
                    # if the page response didnt match to filterd codes return wrong
                    # else check the filterd length with page length
                    if not req_stcode in fstatus:
                        if flength <= int(length):
                            return ["SUCCESS",ipaddr,req_stcode,length]
                        else:
                            return ["WRONG"]
                    else:
                        return ["WRONG"]

                else:
                    # check the filterd length with page length
                    if flength <= int(length):
                            return ["SUCCESS",ipaddr,req_stcode,length]
                    else:
                        return ["WRONG"]

            except requests.exceptions.ConnectionError:
                return ["FAILED"]
            except requests.exceptions.InvalidURL:
                return ["FAILED"]
            except requests.exceptions.ReadTimeout:
                return ["FAILED"]

        run_live_checker = run(TARGET)
        target_ip   = run_live_checker[1]
        status_code = run_live_checker[2]
        res_length  = run_live_checker[3]
        
        # If the response from function was SUCCESS
        # Run the printout_livechecker function to print the results.
        if run_live_checker[0] == "SUCCESS":
            printout_livechecker(TARGET,status_code,target_ip,res_length)
        # Otherwise run the printout function to print the results. 
        else:
           print(TARGET)

        # Check that if User wants to save the results 
        if output:
            spl = str(output).split(":")
            if spl[1].lower() == "raw":
                if run_live_checker[0] == "FAILED":
                    results.append(TARGET)
                else:
                    results.append(f"{TARGET:<30}[ Status: {status_code:<5} | Length: {res_length:<10} | IP: {target_ip} ]")
            
            elif spl[1].lower() == "json":
            
                if run_live_checker[0] == "FAILED":
                    failed.append(TARGET)
                else:
                    results.append({"subdomain":TARGET,"status_code":status_code,"length":res_length,"ip":target_ip})
        

    with ThreadPoolExecutor(max_workers=int(thread)) as executor:
        executor.map(main,urls)
    
    if len(results) > 0:
        spl = str(output).split(":")
        if spl[1].lower() == "raw":
            save(output,results,domain)
        elif spl[1].lower() == "json":
            save(output,results,domain)