from ctypes import *

libc = CDLL("libc.so.6")
mesg = "TralahTek Debugs with ctypes."
libc.printf("Testing: %s" % mesg)
