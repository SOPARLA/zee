# sys library for writing output to the terminal
import sys

# If the -v arg was specified, this function will print the sources results.
def printverb(src,total,duplicates,trues):
    # A normal empty string
    empty = ""
    sys.stdout.write(f"[!] {src:<15} TOTAL {empty:<2}{str(total):<9} DUPLICATES {empty:<2}{str(duplicates):<9} NOT DUPLICATED {empty:<2}{str(trues)}\n")
    
def printverb_error(src,res):
    # A normal empty string
    empty = ""

    sys.stdout.write(f"[!] {src:<15} ERROR {empty:<2}{str(res)}\n")
    

def printout(url):
    sys.stdout.write(f"{url}\n")


def printout_livechecker(url,status,ip,page_length):
    
    empty = ""
    sys.stdout.write(f"{url:<37}[ Status: {status:<5} | Length: {page_length:<10} | IP: {ip:<15} {empty}]\n")