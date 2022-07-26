# sys library for writing output to the terminal
# signal library for identity when client press the ctrl+c and terminate the tool with terminate_tool function in exit file
# time library for setting timeout before running the terminate_tool and time. time() to calculate how many requests are sent in a second.
# concurrent.futures library to make tools faster.
import sys,signal,time,tldextract
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ALL_COMPLETED as COMPLETED

from .save_results import save
from .requester import send_request
from .exit import terminate_tool

def main(arguments):

    global stop,ok_print,results,line,br
    results,line = [],[]
    stop,ok_print,br = False,True,False
    st_time = time.time()
    ls_time = 0

    try:
        # Arguments entered by the user and tool default arguments
        domain = arguments['domain']
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
                sys.stdout.write(f"\x1b[K{url:<27}[ Status: {status_code:<5} | REDIRECTED: {page_headers['Location']:<5} ]\n")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\x1b[K{url:<27}[ Status: {status_code:<5} | Length: {page_length:<10} | IP: {ip:<15} | asn: {asn:<5} ]\n")
                sys.stdout.flush()


        def exitf():
            if not len(results) == 0:
                save(str(output),results,domain)
                terminate_tool()
            else:
                terminate_tool()


        # The persec function is used to calculate the number of requests sent in the last second.
        def persec():
            crt = int(ls_time) - int(st_time)

            if crt > 0:
                rate = len(line) / crt
                if "." in str(rate):
                    rate = int(str(rate).split(".")[0])
            else:
                rate = 0

            if 0 < rate < 1: 
                p = (1 / rate)
                if "." in str(p):
                    return int(str(p).split(".")[0])
                return p
            else:
                return rate


        # MAIN PART
        def run(url):
            line.append(1)
            # Send request
            request = send_request(url=url,header=heads,timeout=timeout,http_method=http_method)

            # Check The response from the send_request function
            if not request == "FAILED":
                asn = request[2]
                ipaddr = request[1]
                domain  = request[0].url
                req_stcode  = request[0].status_code
                req_content = request[0].content
                req_headers = request[0].headers
                subdomain = tldextract.extract(url).subdomain

                # GET THE PAGE RESPONSE SIZE
                if 'content-length' in req_headers:
                    length = req_headers['content-length']
                else:
                    length = len(req_content)

                if not filtered_status == []:
                    # Compare the Response Status Code with Filtered Codes.
                    if not req_stcode in filtered_status:
                        # COMPARE THE LENGTH OF THE RESPONSE WITH FILTERED LENGTHS
                        if filter_length <= int(length):
                            if ok_print:
                                if not silent: 
                                    # print the results in terminal with printout function
                                    printout(url=domain,status_code=req_stcode,ip=ipaddr,asn=asn,page_length=length,page_headers=req_headers)
                                else: 
                                    # print only the url with the write function in the sys library.
                                    sys.stdout.write(f"\x1b[K{domain}\n")
                            if output:
                                arg = str(output).split(":")
                                # If the client sets the output option to -od, saving the asn and ip too
                                if arg[1] == "detail":
                                    results.append(f"{url:<33}[ Status: {req_stcode:<5} | Length: {length:<10} | IP: {ipaddr:<15} | asn: {asn:<5} ]")
                                
                                elif arg[1] == "json":
                                    results.append({"subdomain":subdomain,"status_code":req_stcode,"length":length,"ip":ipaddr,"asn":asn})
                                
                                elif arg[1] == "simple":
                                    results.append(str(domain))
                else:
                    # COMPARE THE LENGTH OF THE RESPONSE WITH FILTERED LENGTHS
                    if filter_length <= int(length):
                        if ok_print:
                            
                            if not silent: 
                                # print the results in terminal with printout function
                                printout(url=url,status_code=req_stcode,ip=ipaddr,asn=asn,page_length=length,page_headers=req_headers)
                            else: 
                                # print only the url with the write function in the sys library.
                                sys.stdout.write(f"\x1b[K{domain}\n")
                            
                            if output:
                                arg = str(output).split(":")
                                # If the client sets the output option to -od, saving the asn and ip too
                                if arg[1] == "detail":
                                    results.append(f"{url:<33}[ Status: {req_stcode:<5} | Length: {length:<10} | IP: {ipaddr:<15} | asn: {asn:<5} ]")
                                
                                elif arg[1] == "json":
                                    results.append({"subdomain":subdomain,"status_code":req_stcode,"length":length,"ip":ipaddr,"asn":asn})
                                
                                elif arg[1] == "simple":
                                    results.append(str(domain))

        # make a thread with the ThreadPoolExecutor function.
        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            executor.map(run,subdomains,timeout=int(timeout))

            while not br:
                ls_time = time.time()
                def sig(signal, frame):
                    global ok_print,br
                    br,ok_print = True,False
                    executor.shutdown(wait=False,cancel_futures=True)
                    exitf()
                signal.signal(signal.SIGINT, sig)

                if len(line) == len(subdomains):
                    br = True

                if not silent:
                    if ok_print:
                        sys.stdout.write(f"[   Line: {len(line):<10}/\tTotal: {len(subdomains):<10}/\tREQ PERSEC: {persec():<3} ]\r")
                        sys.stdout.flush()


        if COMPLETED:
            if not len(results) == 0:
                save(str(output),results,domain)
                terminate_tool()

            terminate_tool()

    except RuntimeError:
        pass
    except KeyboardInterrupt:
        br,ok_print = True,False
        executor.shutdown(wait=False,cancel_futures=True)
        exitf()