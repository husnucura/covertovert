# Import necessary modules from Scapy
from scapy.all import ICMP, IP, sniff

# Define a callback function to process each packet
def packet_callback(packet):
    # Check if the packet contains an ICMP layer
    if packet.haslayer(ICMP):
        # Access the IP layer of the packet
        ip_layer = packet[IP]
        # Check if the TTL of the packet is equal to 1
        if ip_layer.ttl == 1:
            # Show the packet's details
            packet.show()

# Start sniffing for ICMP packets and call the packet_callback function for each packet that matches the filter
sniff(filter="icmp", prn=packet_callback)