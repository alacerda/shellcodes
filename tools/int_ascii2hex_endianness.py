#!/usr/bin/python

import binascii
import sys
from termcolor import colored

txt = sys.argv[1]
n = 4
base="0x01010101"

pieces = [txt[i:i+n] for i in range(0, len(txt), n)]

for reverted in pieces[::-1]:
    if (len(reverted) < n):
        parsed = binascii.hexlify(reverted[::-1])
        parsed = hex(int(parsed,16) + int(base,16))
        print colored("; bypassing Nullbytes restriction", 'green')
        print colored("mov ebx, " + parsed, 'yellow')
        print colored("sub ebx, " + base,'yellow')
        print colored("push ebx" + " ;" + reverted[::-1],'yellow')

    else:
        print("push 0x"+binascii.hexlify(reverted[::-1]) + " ;" + reverted[::-1])

print("mov ebx, esp")

