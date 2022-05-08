<img src="src/wrapper/STATIC/ZEE.png" alt="banner" width="70%">

## *ZEE IS A PYTHON WRITTEN SUBDOMAIN BRUTEFORCE*

![py](https://img.shields.io/badge/WRITTEN%20IN-PYTHON-blue)
![Version](https://img.shields.io/badge/VERSION-1.0-red)
<a href="mailto:bosshbz84@gmail.com">
    ![contact](https://img.shields.io/badge/EMAIL-white?logo=gmail)
</a>

------------

# TABELS

- [INSTALLATION](https://github.com/SOPARLA/zee#INSTALLATION)
    - [ZEE](https://github.com/SOPARLA/zee#ZEE)
    - [REQUIREMENTS](https://github.com/SOPARLA/zee#requirements)
- [EXAMPLE USAGE](https://github.com/SOPARLA/zee#USAGE)
    - [ARGS](https://github.com/SOPARLA/zee#ARGS)
    - [EXAMPLES](https://github.com/SOPARLA/zee#examples)
- [CONFIGURATION FILE](https://github.com/SOPARLA/zee#CONFIG)
- [COMING SOON](https://github.com/SOPARLA/zee#soon)


# INSTALLATION
------------

## ZEE
- git: `git clone https://github.com/SOPARLA/zee.git`
- zip: [Download](https://github.com/SOPARLA/zee/archive/master.zip)

## REQUIREMENTS
```
python 3 or higher
pip install -r requirements.txt
```

# USAGE
------------

### ARGS
```
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
```

### EXAMPLES

```
DEFAULT ( IT EMPLOYS THE TOOL CONFIGURATION FILE DEFAULT ARGUMENT ).

    python zee.py -u https://ZEE.domain.com

CONFIG FILE ( YOU CAN SPECIFY YOUR OWN CONFIG FILE ).

    python zee.py -u https://ZEE.domain.com -config config_file.ini

ENUMRATE SUBDOMAINS FROM WORDLIST WITH 100 THREADS AND 5 SECONDS TIMEOUT
DON'T COLORIZE THE OUTPUT ( YOU CAN CHANGE THE AMOUNT OF ARGUMANTS ).

    python zee.py -u https://ZEE.domain.com -w subdomains.txt -t 100 -timeout 5 -nc

FILTER RESPONSE STATUS CODES 404,403,401 WITH -fs OPTION
FILTER RESPONSE PAGE LENGTH TILL 500 WITH -cl OPTION
SEND REQUESTS WITH THE HEAD HTTP METHOD WITH -hm OPTION, SETTING THE REQUEST HEADERS WITH -header
( YOU CAN CHANGE THE AMOUNT OF ARGUMANTS ).

    python zee.py -u https://zee.domain.com -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us" -fs 404,403,401 -cl 500 -hm head
```

# CONFIGURATION FILE
------------
```ini
[main] # ( PLEASE SPECIFY A SECTION NAME LIKE "main" OR ANYTHING YOU WANT )
timeout = 10
threads = 30
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"  ,"Accept-Language": "*","Accept-Encoding": "*","Accept":"text/html","Referer":"https://www.google.com"}
http_method = get
filter_status = 404,403
silent = False
dont_colorize = False
output = Out.txt
```

# COMING SOON
------------
```
- PASSIVE MODE ( NEW FEATURE ) 
    - MORE THAN 20 PROVIDER FOR SUBDOMAIN ENUMERATION
    - SIMPLE TO USE
    - NEW ARGUMENTS
    - RUN FROM CONFIG

- ACTIVE MODE
    - SENDING REQUESTS FASTER
    - FAST EXIT
    - JSON OUTPUT
```