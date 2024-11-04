from scapy.all import ICMP, IP, sniff

def packet_callback(packet):
    if packet.haslayer(ICMP):
        ip_layer = packet[IP]
        if ip_layer.ttl == 1:
            packet.show()


sniff(filter="icmp", prn=packet_callback)