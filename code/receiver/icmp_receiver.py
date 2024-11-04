from scapy.all import ICMP, IP, sniff

def packet_callback(packet):
    if packet.haslayer(ICMP):
        ip_layer = packet[IP]
        if ip_layer.ttl == 1:
            print("Received ICMP packet with TTL=1:")
            print(packet.show())


print("Starting ICMP receiver...")
sniff(filter="icmp", prn=packet_callback)
