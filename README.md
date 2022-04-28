<img src="src/wrapper/STATIC/ZEE.png" alt="banner" width="80px">

Tables
------------
- [INSTALLATION](https://github.com/SOPARLA/zee#INSTALLATION)
    - [ZEE](https://github.com/SOPARLA/zee#ZEE)
    - [REQUIREMENTS](https://github.com/SOPARLA/zee#requirements)
- [EXAMPLE USAGE](https://github.com/SOPARLA/zee#USAGE)
    - [COMMANDS](https://github.com/SOPARLAzee#COMMANDS)
    - [RUN WITH DEFAULT ARGUMENTS](https://github.com/SOPARLA/zee#DEFAULT)
- [CONFIG FILE](https://github.com/SOPARLA/zee#CONFIG)
- [COMING FEATURES](https://github.com/SOPARLA/zee#soon)


## INSTALLATION

### ZEE
- git: `git clone https://github.com/SOPARLA/zee.git`
- zip: [Download here](https://github.com/SOPARLA/zee/archive/master.zip)
### REQUIREMENTS
    python 3 or higher
    pip install -r requirements.txt

## USAGE

### COMMANDS
    ZEE OPTIONS:
        -u URL                TARGET URL eg. -u https://ZEE.domain.com/ | https://ZEE.subdomain.domain.com/
                              ( PLEASE PUT ZEE IN THE PART THAT YOU WANT TO BRUTEFORCE )

        -w WORDLIST           WORDLIST PATH eg. -w path\subdomains.txt ( DEFAULT: SECLIST-20000 )
        -t THREAD             NUMBER OF THREADS ( DEFAULT: 20 )
        -config CONFIGFILE    CONFIG FILE eg. -config config.ini
        -v                    TOOL VERSION

    HTTP OPTIONS:
        -header HEADER        HTTP HEADERS ( PLEASE PUT THEM IN DOUBLE QUOTES or QUOTES AND SPLIT THEM WITH PIPE | )
                            eg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us"

        -hm HTTPMETHOD        SET HTTP METHOD eg. -hm head ( DEFAULT: GET )
        -timeout TIMEOUT      HTTP request timeout in seconds eg. -timeout 5 ( DEFAULT: 3 )

    FILTER:
        -cl FILTERLENGTH      FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )
        -fs FILTERSTATUS      FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )

    OUTPUT:
        -os SIMPLE_SAVE       SAVE RESULTS SIMPLE OUTPUT eg. -os res.txt ( ONLY TXT FILES )
        -od ADVANCED_SAVE     SAVE THE RESULTS ADVANCED OUTPUT eg. -od res.txt ( ONLY TXT FILES )
        -nc                   DON'T COLORIZE OUTPUT ( DEFAULT: False )
        -silent               ONLY SHOW'S THE RESULTS ( DEFAULT: False )
### DEFAULT
    python zee.py -