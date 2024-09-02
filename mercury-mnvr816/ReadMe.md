
# An unauthenticated web interface in Mercury-MNVR816 Video Recorder

## Overview

    * Type: Information leak
    * Supplier: Mercury
    * Victim URL: http://192.168.1.240/web-static/ 
    * Product: MNVR816
    * Affect version: (lastest) 2.0.1.0.5
    * Firmware download: https://service.mercurycom.com.cn/download-2582.html
 

## Description

An unauthenticated web interface is able to leak local files of the affected video recorder devices. Without any permition, attacker can get sensitive information about the device from the victim URL.

The victime url is a hidden interface and isn't been protected by any authentication and authorization.

## Business Impact

The unauthenticated web interface could lead to serious damage. Thus the vulnerability is very dangerous which could also result in reputational damage for the business through the impact on customers' trust.

## Steps to Reproduce

Visit the victime URL from the web, and you can browse the local files without any permission.
