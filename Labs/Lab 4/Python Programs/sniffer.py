#!/usr/bin/python3
from scapy.all import *
def print_and_send_pkt(pkt): 
	if IP in pkt and ICMP in pkt and pkt [IP].src=="10.10.10.10":
		print("Capturing ICMP Packet:- ")
		pkt.show()
		
		#Constructing a new ICMP packet.
		new_pkt = IP(src=pkt[IP].dst, dst=pkt[IP].src)/ICMP(id=pkt[ICMP].id, seq=pkt[ICMP].seq, type=0)/Raw(load=b'COMP8677-Manjinder Singh')

		#Sending the new packet
		new_pkt.show() 
		send(new_pkt)

#Capture packets
print("SNIFFING PACKETS...")
pkt = sniff(filter="icmp", iface="br-3cb06be4a02f", prn=print_and_send_pkt)

