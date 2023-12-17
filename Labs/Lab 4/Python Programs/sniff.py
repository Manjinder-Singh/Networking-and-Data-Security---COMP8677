#!/usr/bin/python3
from scapy.all import *

print("SNIFFING PACKETS.........")
print("hi")
def print_pkt(pkt):
   print("Source IP:", pkt[IP].src)
   print("Destination IP:", pkt[IP].dst)
   print("Protocol:", pkt[IP].proto)
   print("\n")

pkt = sniff(filter='icmp',iface="br-3cb06be4a02f", count=5, prn=print_pkt)

pkt[2].show2()