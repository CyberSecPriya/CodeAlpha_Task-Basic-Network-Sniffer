from scapy.all import sniff, IP, TCP

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport} -> Destination Port: {tcp_layer.dport}")
        else:
            print("Not a TCP packet.")
        print("-" * 50)

print("Starting network sniffer... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)
