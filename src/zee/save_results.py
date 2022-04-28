from colorama import Fore;import os
def save(file_name,results):
    if not os.path.exists(str(file_name)):
        res_path = open(file_name,"w")
        for last in results:
            res_path.write(str(last)+"\n")
    else:
        question = input(f"\n{Fore.RED}[ERROR] CAN'T SAVE RESULTS\n{Fore.YELLOW}THIS FILE ( {file_name} ) EXISTS DO YOU WANT TO REWRITE IT OR CHANGE FILE NAME OR SKIP SAVING ( Y / C / S ) :> ")
        if question == "y" or question == "Y":
            res_path = open(file_name,"w")
            for last in results:
                res_path.write(str(last)+"\n")
        elif question == "c" or question == "C":
            new_filename = input(Fore.CYAN+f"\nPLEASE ENTER NEW FILENAME :> ")
            res_path = open(new_filename,"w")
            for last in results:
                res_path.write(str(last)+"\n")
        elif question == "" or question == "s" or question == "S":
            pass