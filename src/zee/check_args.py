# In this section, we will handle the user cli

# os library for systematic commands and file existence checks
# io library provides Python’s main facilities for dealing with various types of I/O
# json library for json objects
# sys library for exit function
# platform library used to obtain client distribution
# colorama library for text coloring
# configparser for reading the .ini files data
import sys,os,io,email,json,platform
from colorama import Fore
from .main import main
from src.wrapper import banner
from configparser import ConfigParser,NoOptionError

def check(word_list,url,config_file,heads,status,http_method,timeout,length,thread,silent,colorize,output):

    # default  variables
    word_list_len = ""
    filtered_status = []
    args = {"wordlist":word_list,
            "timeout":timeout,
            "threads":thread,
            "headers":{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"  ,"Accept-Language": "*","Accept-Encoding": "*","Accept":"text/html","Referer":"https://www.google.com"},
            "http_method":"get",
            "filter_length":length,
            "filter_status":[],
            "silent":silent,
            "colorize":colorize,
            "output":output
            }

    # CHECK THE ZEE WORD AND HTTP
    if not("https://" in url or "http://" in url):
        sys.exit(Fore.RED+"\n\n[ERROR] HTTP MISSING\n\teg. https://zee.domain.com")
    elif not ("ZEE." in url or "zee." in url):
        sys.exit(Fore.RED+"\n\n[ERROR] ZEE WORD MISSING\n\teg. https://zee.domain.com or https://ZEE.domain.com")

    # READ FROM CONFIG FILE
    if config_file:
        read_config = ConfigParser(allow_no_value=True)
        if not os.path.exists(config_file):
            sys.exit(Fore.RED+f"\n\n[ERROR] CAN'T FIND {config_file}")
        read_config.read(config_file)
        for section in read_config.sections():
            try:
                
                # GET WORDLIST FOR BRUTEFORCE
                try:
                    data = (read_config.get(section,"wordlist"))
                    if not data == "":
                        args.update({"wordlist":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass
                
                # SET TIMEOUT FOR REQUESTS AND THREADS
                try:
                    data = (read_config.getint(section,"timeout"))
                    if not data == "":
                        args.update({"timeout":data})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass
                
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
                
                # SET REQUESTS HEADERS
                try:
                    data = (read_config.get(section,"headers"))
                    if not data == "":
                        args.update({"headers":json.loads(data)})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

                # HTTP METHOD FOR SENDING REQUESTS
                try:
                    data = (read_config.get(section,"http_method"))
                    if not data == "":
                        args.update({"http_method":data})
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
                
                # SILENT OUTPUT ONLY SHOW THE REUSLTS
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
                        args.update({"output":f"{data}:simple"})
                    else:
                        pass
                except NoOptionError:
                    pass
                except ValueError:
                    pass

            except RuntimeError:
                pass

    # CHECK THE WORDLIST FILE
    if word_list:
        subdomains = []
        if (os.path.exists(word_list)):
            subdomains_file = open(word_list,"r").read().splitlines()
            word_list_len = len(subdomains_file)
            for ex_subs in subdomains_file:
                subdomains.append(str(url).replace("zee",ex_subs).replace("ZEE",ex_subs))
            args.update({'wordlist':subdomains})
        else:sys.exit(Fore.RED+f"\n\n[ERROR] CAN'T FIND {word_list}")
    
    else:
        if (os.path.exists(args["wordlist"])):
            subdomains = []
            subdomains_file = open(args["wordlist"],"r").read().splitlines()
            word_list_len = len(subdomains_file)
            for ex_subs in subdomains_file:
                subdomains.append(str(url).replace("zee",ex_subs).replace("ZEE",ex_subs))
            args.update({'wordlist':subdomains})
        else:sys.exit(Fore.RED+"\n\n[ERROR] PLEASE PROVIDE SUBDOMAINS BECAUSE DEFAULT WORDLIST ( seclist-20000.txt ) FILE IS MISSING")


    # Check if the client set the headers 
    if heads:
        # SEPARATE THE HEADERS
        ex_heads = {}
        for str_to_dict in heads.split("|"):
            ex_heads.update(dict(email.message_from_file(io.StringIO(str_to_dict))))
        args.update({"headers":ex_heads})

    if http_method:
        http_method = str(http_method).lower()
        methods = ['post',"head","options","get"]
        if http_method in methods:
            args.update({"http_method":http_method})
        else:sys.exit(Fore.RED+f"[ERROR] CAN'T SEND REQUEST WITH {http_method}\nTHE DEFAULT METHOD IS GET\nAVAILABLE HTTP METHODS post,head,options,get")

    if status:
        for ex_status_codes in status.split(","):
            filtered_status.append(int(ex_status_codes.strip()))
            args.update({"filter_status":filtered_status})
    
    if not args['silent']:
        opt = platform.system().lower()
        if opt == "windows":
            os.system("cls")
        elif opt == "linux":
            os.system("clear")
        else:
            os.system("clear")
    
        # run the main functoin in banner file
        banner.main(url,word_list,word_list_len,args["http_method"],args["filter_status"],args['timeout'],args["filter_length"],args["threads"],args["colorize"])
    
    main(args)
