# Import necessary modules from Scapy
from scapy.all import ICMP, IP, send

# Create an IP packet with a specified destination address
packet = IP(dst="receiver") / ICMP()

# Set the TTL field of the IP packet to 1
packet.ttl = 1 

# Send the packet to the specified destination
send(packet)