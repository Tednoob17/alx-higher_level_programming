#!/usr/bin/python3
from scapy.all import *
pkt = IP(dst="192.168.43.106")/TCP(dport=80)/"AAAA"
send(pkt)
