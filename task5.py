from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    """Callback function to process each captured packet."""
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

        if packet.haslayer(TCP):
            print("Protocol: TCP")
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload Data: {payload.decode(errors='ignore')}")
        
        print("-" * 50)

def start_sniffing(interface):
    """Start capturing packets on the specified network interface."""
    print(f"Starting packet capture on interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    import argparse

    # Argument parsing
    parser = argparse.ArgumentParser(description='Packet sniffer tool.')
    parser.add_argument('interface', type=str, help='Network interface to sniff on')
    args = parser.parse_args()

    start_sniffing(args.interface)
