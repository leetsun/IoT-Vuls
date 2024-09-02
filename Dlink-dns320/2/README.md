# Info Leak in Dlink-DNS320 NAS

## Overview

    * Type: Information leak
    * Supplier: Dlink
    * Victim URL: http://{Device-IP}/cgi-bin/widget_api.cgi?getSer
    * Product: ShareCenter™ 2-Bay Network Storage Enclosure DNS-320
    * Affect version: (lastest) 2.02b01
    * Firmware download: http://files.dlink.com.au/products/DNS-320/REV_A/Firmware/Firmware_v2.02b01/DNS-320_A1_FW_2.02b01.zip
 

## Description

An infomation leaking vulnerability is at the web management interface of the affected NAS devices. Without any permition, attacker can get sensitive information about service from the victim URL.

The victime url is a hidden interface and isn't been protected by any authentication and authorization.

## Business Impact

The leaked information is sensitive and could result in serious damage. Thus the vulnerability is very dangerous which could also result in reputational damage for the business through the impact on customers' trust.

## Steps to Reproduce

Visit the victime URL from the web, such sensitive information as 'UPNP', 'iTunes', 'FTP' and some configurations are explosed as below:
'''
<UPNP>0</UPNP><iTunes>0</iTunes><FTP>1</FTP><USB>0</USB><model>DNS-320</model><BT>0</BT><HDnum>0</HDnum>
'''
