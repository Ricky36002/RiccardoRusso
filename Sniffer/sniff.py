from scapy.all import *
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse

iPkt= 0
def process_packet(pkt):
    global iPkt
    iPkt += 1
    print("ho letto un pachetto sulla tua macchina " + str(iPkt))

    if not packet.haslayer(IP):
        return
    print(f"IP_SRC: {packet[IP].src} IP_DST: {packet[IP].dst} PROTO: {packet[IP].proto} LEN: {packet[IP].len} ")

    if packet[IP].proto==6:
        print(f"TCP_SRC_PORT: {packet[TCP].sport} TCP_DST_PORT: {packet[TCP].dport}")

        if packet[TCP].sport == 80:
            print(f"HttpResponse")
            if packet.haslayer("HttpResponse"):
                print(packet[HttpResponse].show())
        if packet[TCP].dport == 80:
            print(f"HttpRequest")
            if packet.haslayer("HttpRequest"):
                print(packet[HttpRequest].show())

sniff(iface="enp4s0", filter="tcp", prn=process_packet)

