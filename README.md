<h2>ZEE IS A PYTHON WRITTEN SUBDOMAIN ENUMERATION TOOL</h2>
<img width="900" alt="banner" src="src/wrapper/STATIC/zee.png">

<p align="center">
    <img src="https://img.shields.io/badge/WRITTEN%20IN-PYTHON-blue">
    <img src="https://img.shields.io/badge/VERSION-1.0-orange">
    <a href="mailto:bosshbz84@gmail.com"><img src="https://img.shields.io/badge/EMAIL-white?logo=gmail"></a>
</p>

------------

# TABELS OF CONTENTS
- [ABOUT](#about)
	- [Features](#Features)
	- [Apis](#api)
- [INSTALLATION](#INSTALLATION)
    - [REQUIREMENTS](#requirements)
    - [ZEE](#zee)
- [EXAMPLE USAGE](#USAGE)
    - [ARGS](#ARGS)
        - [ACTIVE](#ACTIVE-ARGS)
        - [PASSIVE](#PASSIVE-ARGS)
    - [EXAMPLES](#examples)
        - [ACTIVE](#ACTIVE-EXAMPLES)
        - [PASSIVE](#PASSIVE-EXAMPLES)
- [CONFIGURATION FILE](#CONFIG)
    - [ACTIVE](#ACTIVE-CONFIG)
    - [PASSIVE](#PASSIVE-CONFIG)

<br>

## ABOUT

### Features
- SUBDOMAIN ENUMERATION BY USING ACTIVE AND PASSIVE METHOD
	- ACTIVE
		- FAST
		- EASY TO USE 
	- PASSIVE
		 - FAST
		 - EASY TO USE
		 - 19 SOURCE FOR SUBDOMAIN COLLECTION

### API 
|SOURCE|API TYPE|
|:---|:---:|
|[alienvault](https://otx.alienvault.com)|NONE|
|[ask](https://www.ask.com)|NONE|
|[binaryedge](https://binaryedge.io/)|API KEY|
|[censys](https://censys.io)|ID & SECRET|
|[certificate details](https://certificatedetails.com)|NONE|
|[certspotter](https://sslmate.com/certspotter/)|NONE|
|[crtsh](https://crt.sh)|NONE|
|[crtshdb](#)|NONE|
|[fullhunt](https://fullhunt.io)|API KEY|
|[hackertarget](https://hackertarget.com/)|NONE|
|[jldc](https://jldc.me)|NONE|
|[jonlu](https://jonlu.ca)|NONE|
|[sonar](https://sonar.omnisint.io)|NONE|
|[passivetotal](https://community.riskiq.com/)|USERNAME & PASSWORD|
|[rappiddns](https://rapiddns.io)|NONE|
|[securitytrails](https://securitytrails.com/)|API KEY|
|[spamhaustech](https://spamhaustech.com)|USERNAME & PASSWORD|
|[threatminer](https://threatminer.org)|NONE|
|[virustotal](https://virustotal.com)|API KEY|

<br>

## INSTALLATION


### REQUIREMENTS

```console
python 3 or higher
```

### ZEE

```console
git clone https://github.com/SOPARLA/zee.git
cd zee
pip install -r requirements.txt
python zee.py
```

<br>

## USAGE

### ACTIVE ARGS
```console
HELP:
  -h, --help

ACTIVE OPTIONS:
  -u TARGET             TARGET URL eg. -u https://ZEE.domain.com/ | https://ZEE.subdomain.domain.com/
                        ( PLEASE PUT ZEE IN THE PART THAT YOU WANT TO BRUTE FORCE )

  -w WORDLIST
                        WORDLIST PATH eg. -w path/subdomains.txt ( DEFAULT: SECLIST-20000 )

  -t THREAD
                        NUMBER OF THREADS ( DEFAULT: 20 )


  -config CONFIGFILE    CONFIG FILE eg. -config config.ini

HTTP OPTIONS:
  -header HEADER        HTTP HEADERS ( PLEASE PUT THEM IN DOUBLE QUOTES or QUOTES AND SPLIT THEM WITH PIPE | )
                        eg. -header "User-Agent: etc|content-type: text/html|Accept-Language: en-Us"

  -hm HTTP VERB
                        SET HTTP VERB eg. -hm head ( DEFAULT: GET )

  -timeout TIMEOUT
                        HTTP request timeout in seconds eg. -timeout 5 ( DEFAULT: 10 )

FILTER:
  -cl FILTER RESPONSE LENGTH
                        FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )

  -fs FILTER STATUS CODE
                        FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )

OUTPUT:
  -o TXT OUTPUT         SAVE THE RESULTS ( ONLY FOUND SUBDOMAIN ) eg. -o res.txt ( ONLY TXT FILES )

  -od TXT OUTPUT WITH DETAILS
                        SAVE THE RESULTS WITH DETAILS ( IP,ASN ...) eg. -od res.txt ( ONLY TXT FILES )

  -oj JSON OUTPUT WITH DETAILS
                        SAVE THE RESULTS IN JSON FORMAT WITH DETAILS eg. -oj res.json

  -nc                   DON'T COLORIZE OUTPUT ( DEFAULT: False )

  -silent               ONLY SHOW'S THE RESULTS ( DEFAULT: False )
```

### PASSIVE ARGS
```console
HELP:
  -h, --help

PASSIVE OPTIONS:
  -u TARGET             TARGET URL eg. -u domain.com

  -ul LIST OF URLS
                        URL LIST eg. -ul urls.txt

  -t THREAD
                        NUMBER OF THREADS ( DEFAULT: 20 )

  -config CONFIGFILE
                        CONFIG FILE eg. -config config.ini

CHECK LIVE:
  -check                CHECK FOR LIVE SUBDOMAINS eg. -check ( DEFAULT: False )

  -cl FILTER RESPONSE LENGTH
                        FILTER PAGE LENGTH  eg. -cl 70 ( DEFAULT: None )

  -fs FILTER STATUS CODE
                        FILTER STATUS CODES eg. -fs 301,302,401,404,502 ( DEFAULT: None )

OUTPUT:
  -o TXT OUTPUT         SAVE THE RESULTS eg. -o res.txt ( ONLY TXT FILES )
  -oj JSON OUTPUT       SAVE THE RESULTS IN JSON FORMAT eg. -oj res.json
  -nc                   DON'T COLORIZE OUTPUT ( DEFAULT: False )
  -v                    VERBOSE MODE ( DEFAULT: False )
  -silent               ONLY SHOW'S THE RESULTS ( DEFAULT: False )
```

<br>

## EXAMPLES

### ACTIVE EXAMPLES

**FOR BRUTE FORCING THE SUBDOMAINS, YOU HAVE TO SPECIFY THE PART THAT YOU WANT TO BRUTE FORCE WITH ZEE OR zee WORD**

#### DEFAULT 

IF YOU DON'T SPECIFY ANY ARGUMENTS THE TOOL WILL RUN WITH DEFAULT CONFIGURATION
```python
$ python zee.py active -u https://ZEE.domain.com
```

#### CONFIG FILE

YOU CAN RUN THE TOOL WITH YOUR OWN CONFIGURATIONS ( IN THE config_examples FOLDER THERE IS AN EXAMPLE OF A CONFIG FILE )
```python
$ python zee.py active -u https://ZEE.domain.com -config config_file.ini
```

#### SECLIST WORDLIST

YOU CAN ENUMERATE SUBDOMAINS WITHOUT A WORLD LIST. THE ZEE WILL SPECIFY THE SECLIST WORDLIST OF 20,000 SUBDOMAINS
```python
$ python zee.py active -u https://ZEE.domain.com -t 100 -timeout 5 -nc
```
<br>

### PASSIVE EXAMPLES

#### DEFAULT 

IF YOU DON'T SPECIFY ANY ARGUMENTS THE TOOL WILL RUN WITH DEFAULT CONFIGURATION
```python
$ python zee.py passive -u domain.com
```

#### CONFIG FILE

YOU CAN RUN THE TOOL WITH YOUR OWN CONFIGURATIONS ( IN THE config_examples FOLDER THERE IS AN EXAMPLE OF A CONFIG FILE )
```python
$ python zee.py passive -u domain.com -config conf.ini
```

#### TARGET LIST

RUN TOOL FASTER WITH -t ARGUMENT, ALSO YOU CAN SPECIFY A LIST OF DOMAINS WITH THE -ul ARGUMENT
```python
$ python zee.py passive -uL urls.txt -t 5
```

#### ONLY SHOW RESULTS

YOU CAN RUN THE TOOL SILENTLY WITH -silent ARGUMENT AND ONLY GET THE RESULTS
```python
$ python zee.py passive -ul urls.txt -silent
```
<br>

#### CHECK FOR LIVE SUBDOMAINS

WITH -check YOU FILTER THE RESULTS -check WILL CHECK FOR LIVE SUBDOMAINS ALSO YOU CAN FILTER THE -check RESULTS.
FOR EXAMPLE WITH -fs YOU CAN FILTER THE LIVE SUBDOMAINS STATUS CODES
WITH -cl YOU CAN FILTER THE LIVE PAGE CONTENT LENGTH
```python
$ python zee.py passive -u domain.com -check -fs 404,403,401 -cl 500
```
<br>

## CONFIG

### ACTIVE CONFIG

```ini
; ( PLEASE SPECIFY A SECTION NAME LIKE "main" OR ANYTHING YOU WANT )
[main]
wordlist = src/general/wordlists/seclist-20000.txt
timeout = 5
threads = 30
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"  ,"Accept-Language": "*","Accept-Encoding": "*","Accept":"text/html","Referer":"https://www.google.com"}
http_method = get
filter_status = 404,403
silent = False
dont_colorize = False
output = Out.txt
```

### PASSIVE CONFIG
```ini
; ( PLEASE SPECIFY A SECTION NAME LIKE "main" OR ANYTHING YOU WANT )
[main]
threads = 10
check = False
filter_length = 0
filter_status = None
silent = False
; dont_colorize = False
; output = Out.txt

[apikeys]
; binaryedge
binaryedge_key = None

; censys
censys_key = None
censys_sec = None

; passivetotal
passivetotal_email = None
passivetotal_password = None

; securitytrails
securitytrails_key = None

; virustotal
virustotal_key = None

; fullhunt
fullhunt_key = None

; spamhaustech
spamhaustech_username = None
spamhaustech_password = None
```