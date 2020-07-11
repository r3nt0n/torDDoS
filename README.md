![[Version 1.0](https://github.com/R3nt0n)](http://img.shields.io/badge/version-v1.0-orange.svg)
![[Python 2.7](https://github.com/R3nt0n)](http://img.shields.io/badge/python-2.7-blue.svg)
![[GPL-3.0 License](https://github.com/R3nt0n)](https://img.shields.io/badge/license-GPL%203.0-brightgreen.svg)
![[Date](https://github.com/R3nt0n)](http://img.shields.io/badge/date-14/07/2019-yellow.svg)


# TorDDos
TorDDos is a Python tool to automatize DDos attacks to a website from the Tor network.
  
<p align="center"><img src="https://github.com/R3nt0n/torDDos/blob/master/img/torddos.png" /></p>


## Usage
```

  -h, --help        show this help message and exit
  -t , --target     server to kick-out
  -n , --attempts   number of attempts of attack (default: 5)

```


## How it works
+ Creates a new Tor session.
+ Makes a request to the website you choose as a target.
+ Releases the Tor session, then creates another and request data again to the website.


## Requirements
+ Linux system
+ Python 2.7
+ Tor service
+ requests


## Legal disclaimer
This tool is created for the sole purpose of security awareness and education, it should not be used against systems that you do not have permission to test/attack. The author is not responsible for misuse or for any damage that you may cause. You agree that you use this software at your own risk.
