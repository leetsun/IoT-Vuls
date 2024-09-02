# Info Leak in Dlink-DNS320 NAS

## Overview

    * Type: Information leak
    * Supplier: Dlink
    * Victim URL: http://{Device-IP}/cgi-bin/widget_api.cgi?getHD
    * Product: ShareCenter™ 2-Bay Network Storage Enclosure DNS-320
    * Affect version: (lastest) 2.02b01
    * Firmware download: http://files.dlink.com.au/products/DNS-320/REV_A/Firmware/Firmware_v2.02b01/DNS-320_A1_FW_2.02b01.zip
 

## Description

An infomation leaking vulnerability is at the web management interface of the affected NAS devices. Without any permition, attacker can get sensitive information about hardware from the victim URL.

The victime url is a hidden interface and isn't been protected by any authentication and authorization.

## Business Impact

The leaked information is sensitive and could result in serious damage. Thus the vulnerability is very dangerous which could also result in reputational damage for the business through the impact on customers' trust.

## Steps to Reproduce

Visit the victime URL from the web, such sensitive information as 'model', 'volume', 'Raid' and some configurations are explosed as below:
'''
<flag>0</flag><model>DNS-320</model><FMT HD></FMT HD><FMT percentage>-1</FMT percentage><HDnum>0</HDnum><volume></volume><usage></usage><volume_no></volume_no><rebuild HD_no></rebuild HD_no><rebuild num>0</rebuild num><rebuild volume></rebuild volume><rebuild time>-1</rebuild time><BT>0</BT><Raid state>0</Raid state>
'''
