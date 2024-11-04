from scapy.all import IP, ICMP, send

packet = IP(dst="receiver") / ICMP()
packet.ttl = 1 
send(packet)
print(f"ICMP request sent to {packet.dst} with TTL={packet.ttl}")
