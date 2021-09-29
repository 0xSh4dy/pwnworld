   0x000000000000114d <+4>:	    push   rbp
   0x000000000000114e <+5>:	    mov    rbp,rsp
   0x0000000000001151 <+8>:	    mov    DWORD PTR [rbp-0x14],edi
   0x0000000000001154 <+11>:	mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001157 <+14>:	sar    eax,0x2
   0x000000000000115a <+17>:	mov    DWORD PTR [rbp-0x4],eax
   0x000000000000115d <+20>:	mov    DWORD PTR [rbp-0xc],0x64
   0x0000000000001164 <+27>:	cmp    DWORD PTR [rbp-0x4],0xa
   0x0000000000001168 <+31>:	jle    0x1178 <func+47>
   0x000000000000116a <+33>:	cmp    DWORD PTR [rbp-0x4],0x13
   0x000000000000116e <+37>:	jg     0x1178 <func+47>
   0x0000000000001170 <+39>:	mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001173 <+42>:	add    DWORD PTR [rbp-0xc],eax
   0x0000000000001176 <+45>:	jmp    0x118f <func+70>
   0x0000000000001178 <+47>:	cmp    DWORD PTR [rbp-0x4],0x5
   0x000000000000117c <+51>:	jle    0x118c <func+67>
   0x000000000000117e <+53>:	cmp    DWORD PTR [rbp-0x4],0x9
   0x0000000000001182 <+57>:	jg     0x118c <func+67>
   0x0000000000001184 <+59>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000001187 <+62>:	add    DWORD PTR [rbp-0xc],eax
   0x000000000000118a <+65>:	jmp    0x118f <func+70>
   0x000000000000118c <+67>:	shl    DWORD PTR [rbp-0xc],1
   0x000000000000118f <+70>:	mov    DWORD PTR [rbp-0x8],0x0
   0x0000000000001196 <+77>:	jmp    0x11a0 <func+87>
   0x0000000000001198 <+79>:	add    DWORD PTR [rbp-0xc],0x1
   0x000000000000119c <+83>:	add    DWORD PTR [rbp-0x8],0x1
   0x00000000000011a0 <+87>:	cmp    DWORD PTR [rbp-0x8],0x4
   0x00000000000011a4 <+91>:	jle    0x1198 <func+79>
   0x00000000000011a6 <+93>:	mov    eax,DWORD PTR [rbp-0xc]
   0x00000000000011a9 <+96>:	imul   eax,eax,0xe9b0
   0x00000000000011af <+102>:	pop    rbp
   0x00000000000011b0 <+103>:	ret    

arg = 19
ans = 12263920