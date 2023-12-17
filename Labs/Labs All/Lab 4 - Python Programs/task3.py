#!/usr/bin/python3
#from scapy.all import *

from scapy.all import sniff

def packet_handler(packet):
    # Define your BPF filter string to capture TCP packets from www.example.com
    bpf_filter = "tcp and src host www.example.com and dst net 10.0.2.0/24"

    # Sniff packets using the filter
    captured_packets = sniff(filter=bpf_filter, count=1)

    # Print the captured packet(s)
    print(captured_packets)
    print("Displaying Captured Packet:-", captured_packets[0].show())

if __name__ == "__main__":
    packet_handler(None)