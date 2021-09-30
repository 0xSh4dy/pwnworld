   0x0000000000001169 <+0>:	endbr64 
   0x000000000000116d <+4>:	push   rbp
   0x000000000000116e <+5>: 	mov    rbp,rsp
   0x0000000000001171 <+8>:	sub    rsp,0x50
   0x0000000000001175 <+12>:	mov    DWORD PTR [rbp-0x44],edi
   0x0000000000001178 <+15>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000001181 <+24>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000001185 <+28>:	xor    eax,eax
   0x0000000000001187 <+30>:	movabs rax,0x6566647362666568
   0x0000000000001191 <+40>:	movabs rdx,0x6e6168697775
   0x000000000000119b <+50>:	mov    QWORD PTR [rbp-0x20],rax
   0x000000000000119f <+54>:	mov    QWORD PTR [rbp-0x18],rdx
   0x00000000000011a3 <+58>:	mov    DWORD PTR [rbp-0x10],0x0
   0x00000000000011aa <+65>:	mov    DWORD PTR [rbp-0x30],0x3
   0x00000000000011b1 <+72>:	lea    rax,[rbp-0x20]
   0x00000000000011b5 <+76>:	mov    QWORD PTR [rbp-0x28],rax
   0x00000000000011b9 <+80>:	movzx  eax,BYTE PTR [rbp-0x1b]
   0x00000000000011bd <+84>:	movsx  eax,al
   0x00000000000011c0 <+87>:	sub    eax,0x30
   0x00000000000011c3 <+90>:	mov    DWORD PTR [rbp-0x2c],eax
   0x00000000000011c6 <+93>:	mov    eax,DWORD PTR [rbp-0x30]
   0x00000000000011c9 <+96>:	mov    edx,DWORD PTR [rbp-0x2c]
   0x00000000000011cc <+99>:	mov    ecx,eax
   0x00000000000011ce <+101>:	sar    edx,cl
   0x00000000000011d0 <+103>:	mov    eax,edx
   0x00000000000011d2 <+105>:	shl    eax,0x2
   0x00000000000011d5 <+108>:	and    eax,0x4a
   0x00000000000011d8 <+111>:	or     eax,0x4
   0x00000000000011db <+114>:	mov    DWORD PTR [rbp-0x2c],eax
   0x00000000000011de <+117>:	mov    BYTE PTR [rbp-0x1b],0x30
   0x00000000000011e2 <+121>:	movzx  eax,BYTE PTR [rbp-0x1c]
   0x00000000000011e6 <+125>:	movsx  eax,al
   0x00000000000011e9 <+128>:	movzx  edx,BYTE PTR [rbp-0x16]
   0x00000000000011ed <+132>:	movsx  edx,dl
   0x00000000000011f0 <+135>:	sub    edx,0x30
   0x00000000000011f3 <+138>:	add    edx,eax
   0x00000000000011f5 <+140>:	movzx  eax,BYTE PTR [rbp-0x19]
   0x00000000000011f9 <+144>:	movsx  eax,al
   0x00000000000011fc <+147>:	sub    eax,0x30
   0x00000000000011ff <+150>:	add    eax,edx
   0x0000000000001201 <+152>:	mov    DWORD PTR [rbp-0x2c],eax
   0x0000000000001204 <+155>:	xor    DWORD PTR [rbp-0x2c],0x13
   0x0000000000001208 <+159>:	mov    eax,DWORD PTR [rbp-0x2c]
   0x000000000000120b <+162>:	sar    eax,0x2
   0x000000000000120e <+165>:	shl    eax,0x4
   0x0000000000001211 <+168>:	mov    DWORD PTR [rbp-0x2c],eax
   0x0000000000001214 <+171>:	mov    eax,DWORD PTR [rbp-0x2c]
   0x0000000000001217 <+174>:	imul   eax,eax,0x3e7
   0x000000000000121d <+180>:	add    eax,0x4e1f
   0x0000000000001222 <+185>:	mov    DWORD PTR [rbp-0x2c],eax
   0x0000000000001225 <+188>:	mov    DWORD PTR [rbp-0x38],0x13
   0x000000000000122c <+195>:	mov    DWORD PTR [rbp-0x34],0x0
   0x0000000000001233 <+202>:	jmp    0x1278 <func+271>
   0x0000000000001235 <+204>:	mov    ecx,DWORD PTR [rbp-0x38]
   0x0000000000001238 <+207>:	movsxd rax,ecx
   0x000000000000123b <+210>:	imul   rax,rax,0x66666667
   0x0000000000001242 <+217>:	shr    rax,0x20
   0x0000000000001246 <+221>:	mov    edx,eax
   0x0000000000001248 <+223>:	sar    edx,1
   0x000000000000124a <+225>:	mov    eax,ecx
   0x000000000000124c <+227>:	sar    eax,0x1f
   0x000000000000124f <+230>:	sub    edx,eax
   0x0000000000001251 <+232>:	mov    eax,edx
   0x0000000000001253 <+234>:	shl    eax,0x2
   0x0000000000001256 <+237>:	add    eax,edx
   0x0000000000001258 <+239>:	sub    ecx,eax
   0x000000000000125a <+241>:	mov    edx,ecx
   0x000000000000125c <+243>:	mov    ecx,DWORD PTR [rbp-0x2c]
   0x000000000000125f <+246>:	mov    eax,ecx
   0x0000000000001261 <+248>:	shl    eax,0x2
   0x0000000000001264 <+251>:	add    eax,ecx
   0x0000000000001266 <+253>:	add    edx,eax
   0x0000000000001268 <+255>:	mov    eax,DWORD PTR [rbp-0x38]
   0x000000000000126b <+258>:	imul   eax,DWORD PTR [rbp-0x2c]
   0x000000000000126f <+262>:	add    eax,edx
   0x0000000000001271 <+264>:	mov    DWORD PTR [rbp-0x38],eax
   0x0000000000001274 <+267>:	add    DWORD PTR [rbp-0x34],0x1
   0x0000000000001278 <+271>:	cmp    DWORD PTR [rbp-0x34],0x1
   0x000000000000127c <+275>:	jle    0x1235 <func+204>
   0x000000000000127e <+277>:	mov    eax,DWORD PTR [rbp-0x2c]
   0x0000000000001281 <+280>:	mov    rsi,QWORD PTR [rbp-0x8]
   0x0000000000001285 <+284>:	xor    rsi,QWORD PTR fs:0x28
   0x000000000000128e <+293>:	je     0x1295 <func+300>
   0x0000000000001290 <+295>:	call   0x1060 <__stack_chk_fail@plt>
   0x0000000000001295 <+300>:	leave  
   0x0000000000001296 <+301>:	ret 
arg = 25
ans = 979039
