from scapy.all import *
iPkt= 0
def process_packet(pkt):
    global iPkt
    iPkt += 1
    print("ho letto un pachetto sulla tua macchina " + str(iPkt))

sniff(iface="enp4s0", filter="tcp", prn=process_packet)

