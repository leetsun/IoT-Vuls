# Command injection at the web management interface of Motorola-CX2L

## Overview

    * Type: command injection
    * Supplier: Motorola
    * Product: CX2L, firmware version 1.0.1
    * Affect version: 1.0.1

## Description of the Vulnerability

A command injection vulnerability exists that allows commands to be executed remotely on motorola router CX2L by crafting a request within the web application where there should be no context to access or execute code.

This command injection happened when configuring the SetStaticRouteSettings, the 'staticroute_list' parameter will carry the user's data which isn't sanitized. With an elaborately crafted payload into the 'staticroute_list' parameter, the device will execute the command in the payload.

The vulnerability allows a malicious attacker authenticated on the web to execute commands on the device, enabling an attacker to gain the highest privilege of the system and take over the device.


## Steps to Reproduce

I have put the PoC (exp.py) in the attachments.  Configure several parameters, and execute it, you will see an outputting ping echo from the target device(that is the injected command has been executed). The parameters are as below:
1. password: which is used to login in to the web.
2. device_web_ip: web IP address of the target device.
3. ping_target: Usually configured as the local host. The device will send a ping echo to this host.

## Proof of Concept

You can open Wireshark to monitor the ICMP flow. After executing the PoC, you will see a ping echo from the device to the 'ping_target' host.
