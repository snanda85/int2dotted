#!/usr/bin/env python
"""
Convert IP formats (integer and dotted)
Support IPv4 and IPv6 addresses

Notes:
    If Integer is passed, it will be converted to IP
    If IP address is passed, it will be converted to Integer
.. moduleauthor:: Sandeep Nanda <snanda85@gmail.com>
"""

# NOTICE: Modified from the original code of Sandeep Nanda by Dan Gayle

################################################################################
#   Copyright 2014 Sandeep Nanda
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
################################################################################

import sys
import struct
import socket
import argparse

MAX_INT64 = 0xFFFFFFFFFFFFFFFF

def ip2int(addr):
    """Convert the IP notation to Integer.

    >>> ip2int('8.8.8.8')
    134744072
    >>> ip2int('2001:4860:4860::8888')
    42541956123769884636017138956568135816L
    """
    try:
        # Try IPv4
        return struct.unpack("!i", socket.inet_pton(socket.AF_INET, addr))[0]
    except socket.error:
        # Try IPv6
        hi, lo = struct.unpack("!qq", socket.inet_pton(socket.AF_INET6, addr))
        return (hi << 64) | lo

def int2ip(addr):
    """Convert an Integer to the corresponding IP notation.

    >>> int2ip(134744072)
    '8.8.8.8'
    >>> int2ip(42541956123769884636017138956568135816L)
    '2001:4860:4860::8888'
    """
    try:
        # Try IPv4
        return socket.inet_ntoa(struct.pack("!i", addr))
    except:
        # Try IPv6
        int_tuple = ((addr >> 64) & MAX_INT64, addr & MAX_INT64)
        x = struct.pack("!2q", *int_tuple)
        return socket.inet_ntop(socket.AF_INET6, x)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        argument_default=argparse.SUPPRESS
        )
    parser.add_argument("ip",
        help="IP address in dotted or integer notation.")

    args = parser.parse_args()

    if args.ip:
        try:
            print ip2int(args.ip)
        except:
            try:
                print int2ip(int(args.ip))
            except:
                print int2ip(long(args.ip))

if __name__ == '__main__':
    sys.exit(main())
