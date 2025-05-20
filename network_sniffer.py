from scapy.all import sniff, IP, TCP  # Import necessary modules from Scapy

# Function to process each captured packet
def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]  # Extract the IP layer from the packet
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")  # Print source and destination IP addresses

        # Check if the packet has a TCP layer
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]  # Extract the TCP layer from the packet
            # Print source and destination ports from the TCP layer
            print(f"Source Port: {tcp_layer.sport} -> Destination Port: {tcp_layer.dport}")
        else:
            print("Not a TCP packet.")  # Inform if the packet does not have TCP layer

        print("-" * 50)  # Separator line for readability

# Starting message for user
print("Starting network sniffer... Press Ctrl+C to stop.")

# Start sniffing packets, apply process_packet function on each, and do not store packets in memory
sniff(prn=process_packet, store=False)

