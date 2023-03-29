import sys
from scapy.all import *

def parse(packet):
	flag=packet['TCP'].flags
	if flag == 0x40:
		char = chr(packet['TCP'].sport)
	        sys.stdout.write(char)

sniff(filter="tcp", prn=parse)