import sys,signal,time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ALL_COMPLETED as COMPLETED
from colorama import Fore
from .save_results import save
from .requester import send_request
from .exit import mes,killproc

def main(arguments):
    
    global stop
    global ok_print
    global results
    global line
    global br
    line = []
    results = []
    stop = False
    ok_print = True
    br = False
    st_time = str(time.time()).split(".")[0]
    ls_time = 0

    try:


        subdomains = arguments['wordlist']
        heads = arguments['headers']
        timeout = arguments['timeout']
        http_method = arguments['http_method']
        filtered_status = arguments['filter_status']
        filter_length = arguments['filter_length']
        threads = arguments['threads']
        silent = arguments['silent']
        output = arguments['output']


        # PRINT REQUEST RESULTS
        def printout(url,status_code,ip,asn,page_length,page_headers):
            if "https://" in url or "http://" in url:
                url = str(url).replace("https://","").replace("http://","")
            if str(status_code).startswith("3"):
                sys.stdout.write(f"\x1b[K{url:<26}[ Status: {status_code:<5} | REDIRECTED: {page_headers['Location']:<5} ]\n")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\x1b[K{url:<26}[ Status: {status_code:<5} | Length: {page_length:<10} | IP: {ip:<15} | asn: {asn:<5} ]\n")
                sys.stdout.flush()

        def persec():
            cr = int(ls_time) - int(st_time)
            if cr > 0:
                rate = len(line) / cr
                if "." in str(rate):
                    rate = int(str(rate).split(".")[0])
            else: rate = 0
            
            if 0 < rate < 1: return  (1.0 / rate)
            else: return rate


        # MAIN PART
        def run(url):

            line.append(1)
            request = send_request(url=url,header=heads,timeout=timeout,http_method=http_method)
            if not request == "FAILED":

                asn = request[2]
                ipaddr = request[1]
                req_stcode  = request[0].status_code
                req_content = request[0].content
                req_headers = request[0].headers
                
                # GET THE PAGE RESPONSE SIZE
                if 'content-length' in req_headers:
                    length = req_headers['content-length']
                else:
                    length = len(req_content)

                if not filtered_status == []:
                    
                    # COMPARE THE STATUS CODE WITH FILTERED CODES
                    if not req_stcode in filtered_status:
                    
                        # COMPARE THE RESPONSE LENGTH WITH FILTERED LENGTHS
                        if filter_length <= int(length):
                            
                            if ok_print:
                                if not silent: 
                                    printout(url=url,status_code=req_stcode,ip=ipaddr,asn=asn,page_length=length,page_headers=req_headers)
                                else: 
                                    sys.stdout.write(f"\x1b[K{url}\n")
                            
                            if output:
                                arg = str(output).split(":")
                                if arg[1] == "advanced":
                                    results.append(f"{url:<26}[ Status: {req_stcode:<5} | Length: {length:<10} | IP: {ipaddr:<15} | asn: {asn:<5} ]")
                                else:
                                    results.append(str(url))

                else:

                    # COMPARE THE RESPONSE LENGTH WITH FILTERED LENGTHS
                    if filter_length <= int(length):
                        if ok_print:
                            if not silent: 
                                printout(url=url,status_code=req_stcode,ip=ipaddr,asn=asn,page_length=length,page_headers=req_headers)
                            else: 
                                sys.stdout.write(f"\x1b[K{url}\n")
                        
                        if output:
                            arg = str(output).split(":")
                            if arg[1] == "advanced":
                                results.append(f"{url:<37}[ Status: {req_stcode:<5} | Length: {length:<10} | IP: {ipaddr:<15} | asn: {asn:<5} ]")
                            else:
                                results.append(str(url))

        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            executor.map(run,subdomains,timeout=timeout)
            
            while not br:
                ls_time = str(time.time()).split(".")[0]
                def sig(signal, frame):
                    
                    global ok_print
                    global br
                    br = True
                    ok_print = False
                    executor.shutdown(wait=False,cancel_futures=True)
                    
                    if not len(results) == 0:
                        save(file_name=str(output).split(":")[0],results=results)
                    time.sleep(0.5)
                    mes()
                signal.signal(signal.SIGINT, sig)
                
                if len(line) == len(subdomains):
                    br = True
                
                if not silent:
                    if ok_print:
                        sys.stdout.write(f"[ Line: {len(line):<10}/\tTotal: {len(subdomains):<10}/\tREQ PERSEC: {persec()} ]\r")
                        sys.stdout.flush()

        if COMPLETED:
            if not len(results) == 0:
                save(file_name=str(output).split(":")[0],results=results)
            killproc()
    
    except RuntimeError:
        pass
    
    except KeyboardInterrupt:
        br = True
        ok_print = False
        executor.shutdown(wait=False,cancel_futures=True)
        if not len(results) == 0:
            save(file_name=str(output).split(":")[0],results=results)
        time.sleep(0.5)
        mes()