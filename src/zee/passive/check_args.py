# In this section, we will handle the user cli

# os library for systematic commands and file existence checks
# platform library used to obtain client distribution
# colorama library for colorize terminal.
# configparser for reading the .ini files data
import os,platform
from colorama import Fore
from .main import main
from src.wrapper import banner
from configparser import ConfigParser,NoOptionError

def check(url_list,url,config_file,threads,cl,fstatus,flength,silent,colorize,output,verbose):

    # default  variables
    url_len = ""
    filtered_status = []

    args = {"url":"None",
            "urls":"None",
            "threads":20,
            "check_live":False,
            "filter_length":0,
            "filter_status":[],
            "silent":False,
            "colorize":False,
            "output":output,
            "verbose_mode":False
            }
    
    tokens = {
            "binaryedge_api":"",
            "censys_api":"",
            "censys_pas":"",
            "passivetotal_email":"",
            "passivetotal_pass":"",
            "securitytrails":"",
            "virustotal":"",
            "fullhunt":"",
            "spamhaustech_username":"",
            "spamhaustech_password":""
            }

    # Fixing the URL
    if url:
        if ("https://" in url or "http://" in url):
            url = str(url).replace("https://","").replace("http://","")
            args.update({'url':url})
        else:
            args.update({'url':url})

    # IF -config WAS USED READ FROM FILE CONFIG FILE
    if config_file:
        read_config = ConfigParser(allow_no_value=True)
        if not os.path.exists(config_file):
            exit(Fore.RED+f"\n[ERROR] CAN'T FIND {Fore.WHITE}{config_file}\n")
        read_config.read(config_file)
        for section in read_config.sections():
            try:
                
                # SET WORKERS NUMBER
                try:
                    data = (read_config.getint(section,"threads"))
                    if not data == '':
                        args.update({"threads":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                # SET THE CHECK ARG
                try:
                    data = (read_config.getboolean(section,"check"))
                    if not data == "":
                        args.update({"check_live":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                
                # FILTER RESPONSE PAGE LENGTH
                try:
                    data = (read_config.getint(section,"filter_length"))
                    if not data == "":
                        args.update({"filter_length":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                # SET FILTERED CODES
                try:
                    data = (read_config.get(section,"filter_status"))
                    if not data == "":
                        for ex_status_codes in data.split(","):
                            filtered_status.append(int(ex_status_codes.strip()))
                        args.update({"filter_status":filtered_status})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass
                
                # SHOW ONLY THE FINDED SUBDOMAINS WITH SILENT OUTPUT
                try:
                    data = (read_config.getboolean(section,"silent"))
                    if not data == "":
                        args.update({"silent":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                # DONT COLORIZE THE TERMINAL
                try:
                    data = (read_config.getboolean(section,"dont_colorize"))
                    if not data == "":
                        args.update({"colorize":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass
                
                # SAVE RESULTS
                try:
                    data = (read_config.get(section,"output"))
                    if not data == "":
                        if not data.lower().endswith(".txt") and not data.lower().endswith(".json"):
                            exit(Fore.RED+f"\n[ERROR] WRONG OUTPUT FILE EXTENSION in {Fore.WHITE}{config_file}\n\tPLEASE SPECIFY ONLY .json OR .txt FILE\n")
                        else:
                            if data.lower().endswith(".txt"):
                                args.update({"output":f"{data}:raw"})
                            elif data.lower().endswith(".json"):
                                args.update({"output":f"{data}:json"})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

            # EXTRACT API TOKENS

                try:
                    data = (read_config.get(section,"binaryedge_key"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"binaryedge_api":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"censys_key"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"censys_api":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"censys_sec"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"censys_pas":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"passivetotal_email"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"passivetotal_email":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"passivetotal_password"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"passivetotal_pass":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"securitytrails_key"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"securitytrails":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"virustotal_key"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"virustotal":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"spamhaustech_username"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"spamhaustech_username":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                try:
                    data = (read_config.get(section,"spamhaustech_password"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"spamhaustech_password":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass


                try:
                    data = (read_config.get(section,"fullhunt_key"))
                    if not data == '' and not data == "None" and not data == "none":
                        tokens.update({"fullhunt":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

            except RuntimeError:
                pass

    if not args["check_live"] and args["filter_length"] or args["filter_status"]:
        exit(f"\n{Fore.RED}[ERROR] SORRY, CAN'T ACTION -fs OR -cl WHEN THERE IS NO -check ARGUMENT\n\t{Fore.WHITE}eg. python zee.py -check -fs 404,401 -cl 500")

    # CHECK THE URL LIST FILE
    if url_list:
        domains = []
        if (os.path.exists(url_list)):
            get_domains = open(url_list,"r").read().splitlines()
            
            if len(get_domains) > 0:
                url_len = str(len(get_domains))
                for ex_dom in get_domains:
                    if ("https://" in ex_dom or "http://" in ex_dom):
                        domains.append(str(ex_dom).replace("https://","").replace("http://",""))
                    else:
                        domains.append(str(ex_dom))

                args.update({'urls':domains})

            else:exit(Fore.RED+f"\n[ERROR] THE {url_list} IS EMPTY\n")
       
        else:exit(Fore.RED+f"\n[ERROR] CAN'T FIND {Fore.WHITE}{url_list}\n")
    
    if fstatus:
        for ex_status_codes in fstatus.split(","):
            filtered_status.append(int(ex_status_codes.strip()))
            args.update({"filter_status":filtered_status})
    
    if threads:
        args.update({'threads':threads})
    
    if cl:
        args.update({'check_live':cl})
    
    if flength:
        args.update({'filter_length':flength})
    
    if silent:
        args.update({'silent':silent})
    
    if colorize:
        args.update({'colorize':colorize})
    
    if verbose:
        args.update({'verbose_mode':verbose})


    if not args['silent']:
        opt = platform.system().lower()
        if opt == "windows":
            os.system("cls")
        elif opt == "linux":
            os.system("clear")
        else:
            os.system("clear")
    
        # run the main function in banner file
        banner.passive_banner(url,url_list,url_len,args["filter_status"],args["filter_length"],args["threads"],args["colorize"])
    else:
        args.update({"colorize":True})

    main(args,tokens)
