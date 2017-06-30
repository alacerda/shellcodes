#!/usr/bin/python
#
# rri stands for Reverse Random Insertion
#
# Author: Alan Lacerda (alacerda)
#

import random

shellcode =  \
"\xeb\x14\x4d\x61\x6e\x64\x61\x20\x76\x65\x72\x20\x63\x61\x6d\x61\x72\x61\x64\x61\x21\x0a\x48\x31\xc0\x48\x83\xc0\x01\x48\x89\xc7\x48\x8d\x35\xdb\xff\xff\xff\x48\x31\xd2\x48\x83\xc2\x14\x0f\x05\x48\x31\xc0\x48\x83\xc0\x3c\x48\x31\xff\x48\x83\xc7\x01\x0f\x05"

reverse = bytearray(shellcode[::-1])

encode_1 = ""
encode_2 = ""

for x in bytearray(shellcode):
    encode_1 += '\\x'
    encode_1 += '%02x' % x
    encode_1 += '\\x%02x' % reverse[random.randint(1,len(shellcode) - 1)]

    encode_2 += '0x'
    encode_2 += '%02x,' % x
    encode_2 += '0x%02x,' % reverse[random.randint(1,len(shellcode) - 1)]

print "\n\tWe've generated two different encodes for you. Choose yours!"

print "\nFirst Encode:"
print encode_1

print "\nSecond Encode:"
print encode_2[:-1]
