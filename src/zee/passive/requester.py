# IMPORT SUBDOMAIN FINDERS FROM SOURCES FOLDER
# concurrent LIBRARY FOR SENDING REQUESTS FASTER
from .sources import *
from .print_results import printverb,printverb_error
from concurrent.futures import ThreadPoolExecutor

def send_request(TARGET,workers,apis,verb):
    global true_subdomains
    dups = []
    true_subdomains = 0
    subdomains = []

    # SUBDOMAIN FINDERS functionS
    requests = [
            run_jldc,
            run_crtsh,
            run_censys,
            run_crtshdb,
            run_omnisint,
            run_fullhunt,
            run_rapiddns,
            run_bufferover,
            run_binaryedge,
            run_alienvault,
            run_virustotal,
            run_certspotter,
            run_spamhaustech,
            run_hackertarget,
            run_passivetotal,
            run_securitytrails
        ]


    def run(func):
        # Run the function and get results
        func_res = func(str(TARGET),apis)
        # GET THE SOURCE NAME
        name = str(func_res[0]).rstrip()
        # GET THE LENGTH OF THE FOUNDED SUBDOMAINS
        true_subdomains = len(subdomains)

        # IF RETURNED RESULT EQUELS TO ERROR SHOW ERROR MESSAGE
        if str(func_res[-1]).rstrip() == "ERROR":
            if verb:
                printverb_error(name,func_res[1])
        else:
            # EXTRACT RESULTS
            for ex_subs in func_res[1]:
                if not ex_subs in subdomains:
                    subdomains.append(ex_subs)
                else:
                    dups.append(1)
            
            if verb:
                # INFORM THE USER IF VERB ARG WAS TRUE
                printverb(name,len(func_res[1]),len(dups),(len(subdomains)-true_subdomains))
        
        dups.clear()
        true_subdomains = 0

    # RUN TOOL
    with ThreadPoolExecutor(max_workers=int(workers)-8) as executor:
        executor.map(run,requests)
    
    return subdomains