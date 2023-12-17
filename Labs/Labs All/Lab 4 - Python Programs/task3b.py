from scapy.all import sniff

def packet_handler(packet):
    # Define your BPF filter string to capture packets from source port 53
    # and a specific network (e.g., 10.10.10.0/24)
    bpf_filter = "src port 53 and net 10.10.10.0/24"

    # Sniff packets using the filter
    captured_packets = sniff(filter=bpf_filter, count=1)

    # Print the captured packet(s)
    print(captured_packets[0].show())

if __name__ == "__main__":
    packet_handler(None)
