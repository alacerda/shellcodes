#!/usr/bin/python
#
# rri stands for Reverse Random Insertion
#
# Author: Alan Lacerda (alacerda)
#

import random

shellcode = "\x48\x5b\x90"
reverse = bytearray(shellcode[::-1])

encode_1 = ""
encode_2 = ""

for x in bytearray(shellcode):
    encode_1 += '\\x'
    encode_1 += '%02x' % x
    encode_1 += '\\x%02x' % reverse[random.randint(1,len(shellcode) - 1)]

    encode_2 += '0x'
    encode_2 += '%02x,' % x
    encode_2 += 'x%02x,' % reverse[random.randint(1,len(shellcode) - 1)]

print "\n\tWe've generated two different encodes for you. Choose yours!"

print "\nFirst Encode:"
print encode_1

print "\nSecond Encode:"
print encode_2[:-1]
