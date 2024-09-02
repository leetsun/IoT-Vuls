# Info Leak in Dlink-DNS320 NAS

## Overview

    * Type: Information leak
    * Supplier: Dlink
    * Victim URL: http://{Device-IP}/cgi-bin/widget_api.cgi?getSys
    * Product: ShareCenter™ 2-Bay Network Storage Enclosure DNS-320
    * Affect version: (lastest) 2.02b01
    * Firmware download: http://files.dlink.com.au/products/DNS-320/REV_A/Firmware/Firmware_v2.02b01/DNS-320_A1_FW_2.02b01.zip
 

## Description

An infomation leaking vulnerability is at the web management interface of the affected NAS devices. Without any permition, attacker can get sensitive information about system from the victim URL.

The victime url is a hidden interface and isn't been protected by any authentication and authorization.

## Business Impact

The leaked information is sensitive and could result in serious damage. Thus the vulnerability is very dangerous which could also result in reputational damage for the business through the impact on customers' trust.

## Steps to Reproduce

Visit the victime URL from the web, such sensitive information as 'hostname', 'IP address', 'firmware version' and some configurations are explosed as below:
'''
<hostname>dlink-94CBD4</hostname><IP>192.168.1.110</IP><tempF>115</tempF><tempC>46</tempC><version>2.02b01</version><HDnum>0</HDnum><model>DNS-320<model><BT>0</BT>
'''
