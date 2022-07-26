# SIGNLA FOR DETECTING THE CTRL+C
import signal
from .save_results import save
from .live_checker import live
from .requester import send_request
from .exit import terminate_tool

def main(arguments,apis):
    global ok_print,results
    ok_print = True
    results = []

    # Arguments entered by the user and tool default arguments
    url = arguments['url']
    url_list = arguments['urls']
    thread = arguments['threads']
    check_live = arguments['check_live']
    filter_length = arguments['filter_length']
    filter_status = arguments['filter_status']
    silent = arguments['silent']
    output = arguments['output']
    verb = arguments['verbose_mode']


    try:
        # This function will detect CTRL+C
        def sig(signal, frame):
            global ok_print
            ok_print = False
            terminate_tool()
        signal.signal(signal.SIGINT, sig)
        
        if verb and not silent:
                print(f"[INFO] GATHERING SUBDOMAINS\n")

        if not url == "None":

            data = send_request(url,thread,apis,verb)
            if check_live:
                if verb and not silent:
                    print(f"\n[INFO] CHECKING FOR LIVE SUBDOMAINS\n")
                live(data,filter_status,filter_length,thread,output,url)

            else:
                if not silent:
                    print()

                for last in data:
                    if ok_print:
                        print(last)

                if not silent:
                    print()

                if output:
                    save(output,data,url)

        if not url_list == "None":

            for ex_urls in url_list:    
                if ok_print:
                    if not silent:
                        print(f"\n[!] [{ex_urls}]\n")
                
                data = send_request(ex_urls,thread,apis,verb)
                
                if check_live:
                    if verb and not silent:
                        print(f"\n[INFO] CHECKING FOR LIVE SUBDOMAINS\n")
                    live(data,filter_status,filter_length,thread,output,ex_urls)
                
                else:
                    if not silent:
                        print()

                    for last in data:
                        if ok_print:
                            print(last)
                    if not silent:
                        print()

                if output:
                    save(output,data,ex_urls)
        
        terminate_tool()


    except KeyboardInterrupt:
        ok_print = False
        terminate_tool()