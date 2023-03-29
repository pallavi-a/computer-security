import sys
from scapy.all import *

packet = None

def usage():
	if len(sys.argv) != 2:
		print ("Usage:" + sys.argv[0] + "<host_ip>")
		sys.exit()

def craft(character):
	global packet
	global dest
	dest = str(sys.argv[1])
	char = ord(character)
	packet=IP(dst=dest)/TCP(sport=char, dport=RandNum(0, 65535), flags="E")
	return packet

def client():
	while True:
		message = raw_input('Enter the message: ')
		message += "\n"
		print("Sending data: " + message)
		for char in message:
			newPacket = craft(char)
			send(newPacket)

usage()
client()