#!/usr/bin/env python
"""
Convert IP formats (integer and dotted)
Support IPv4 and IPv6 addresses

 Usage:
    ./int2dotted.py <Integer Or IP>

.. moduleauthor:: Sandeep Nanda <snanda85@gmail.com>
"""
import sys
import struct
import socket
MAX_INT64 = 0xFFFFFFFFFFFFFFFF


def ip2int(addr):
    """Converts the IP notation to Integer"""
    try:
        # Try IPv4
        return struct.unpack("!i", socket.inet_pton(socket.AF_INET, addr))[0]
    except socket.error:
        # Try IPv6
        hi, lo = struct.unpack("!qq", socket.inet_pton(socket.AF_INET6, addr))
        return (hi << 64) | lo

def int2ip(addr):
    """Converts an Integer to the corresponding IP notation"""
    try:
        # Try IPv4
        return socket.inet_ntoa(struct.pack("!i", addr)) 
    except:
        # Try IPv6
        int_tuple = ((addr >> 64) & MAX_INT64, addr & MAX_INT64)
        x = struct.pack("!2q", *int_tuple)
        return socket.inet_ntop(socket.AF_INET6, x)

def print_usage():
    print("Usage:")
    print("\t./int2dotted.py <Integer or IP>")
    print("\nNotes:")
    print("\tIf Integer is passed, it will be converted to IP")
    print("\tIf IP address is passed, it will be converted to Integer")
    sys.exit(1)

if len(sys.argv) != 2:
    print_usage()

arg = sys.argv[1]
if arg.lower() in ("-h", "--help"):
    print_usage()

try:
    ip = int(arg)
except Exception as e:
    #print "Converting IP to Int"
    print ip2int(arg)
else:
    #print "Converting Int to IP"
    print int2ip(ip)
