from scapy.all import ICMP, IP, sniff

def packet_callback(packet):
    if packet.haslayer(ICMP):
        ip_layer = packet[IP]
        if ip_layer.ttl == 1:
            packet.show()

# Start sniffing for ICMP packets and call the packet_callback function for each packet that matches the filter
sniff(filter="icmp", prn=packet_callback)