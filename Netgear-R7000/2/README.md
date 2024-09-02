# DoS Attack in Netgear-R7000 Router

## Overview

    * Type: Dos Attack
    * Supplier: Netgear (https://www.netgear.com/)
    * Victim URL: http://192.168.1.1/WIZ_fix.htm (hidden page)
    * Product: R7000 —  Nighthawk AC1900 Smart WiFi Dual Band Gigabit Router
    * Affect version: V1.0.11.136_10.2.120
    * Firmware download: https://www.downloads.netgear.com/files/GDC/R7000/R7000-V1.0.11.136_10.2.120.zip
    Note: The latest firmware has patch this vul about one month ago. The latest verison: https://www.downloads.netgear.com/files/GDC/R7000/R7000-V1.0.11.216.zip
 

## Description

The vulnerability casuse the device's service down remotely on the device by crafting a request to the web where there should be no context to access. More seriously, the status can only be recovered under resetting the device to the initial factory settings.


## Steps to Reproduce

I have put the PoC (exp.py) in the attachments. The parameters are as below:
1. username, password: normal user (default: admin, password).
2. device_web_ip: web IP address of the target device.
