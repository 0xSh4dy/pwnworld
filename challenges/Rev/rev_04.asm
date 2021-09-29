   0x0000000000001169 <+0>:	    endbr64 
   0x000000000000116d <+4>:  	push   rbp
   0x000000000000116e <+5>:	    mov    rbp,rsp
   0x0000000000001171 <+8>: 	sub    rsp,0x30
   0x0000000000001175 <+12>:	mov    rax,QWORD PTR fs:0x28
   0x000000000000117e <+21>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000001182 <+25>:	xor    eax,eax
   0x0000000000001184 <+27>:	lea    rax,[rip+0xe79]        # 0x2004
   0x000000000000118b <+34>:	mov    QWORD PTR [rbp-0x28],rax
   0x000000000000118f <+38>:	mov    DWORD PTR [rbp-0x30],0x0
   0x0000000000001196 <+45>:	jmp    0x11b5 <func+76>
   0x0000000000001198 <+47>:	mov    eax,DWORD PTR [rbp-0x30]
   0x000000000000119b <+50>:	movsxd rdx,eax
   0x000000000000119e <+53>:	mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000011a2 <+57>:	add    rax,rdx
   0x00000000000011a5 <+60>:	movzx  edx,BYTE PTR [rax]
   0x00000000000011a8 <+63>:	mov    eax,DWORD PTR [rbp-0x30]
   0x00000000000011ab <+66>:	cdqe   
   0x00000000000011ad <+68>:	mov    BYTE PTR [rbp+rax*1-0x20],dl
   0x00000000000011b1 <+72>:	add    DWORD PTR [rbp-0x30],0x1
   0x00000000000011b5 <+76>:	cmp    DWORD PTR [rbp-0x30],0x7
   0x00000000000011b9 <+80>:	jle    0x1198 <func+47>
   0x00000000000011bb <+82>:	movzx  eax,BYTE PTR [rbp-0x1c]
   0x00000000000011bf <+86>:	movsx  eax,al
   0x00000000000011c2 <+89>:	sub    eax,0x30
   0x00000000000011c5 <+92>:	mov    DWORD PTR [rbp-0x2c],eax
   0x00000000000011c8 <+95>:	mov    eax,DWORD PTR [rbp-0x2c]
   0x00000000000011cb <+98>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x00000000000011cf <+102>:	xor    rcx,QWORD PTR fs:0x28
   0x00000000000011d8 <+111>:	je     0x11df <func+118>
   0x00000000000011da <+113>:	call   0x1060 <__stack_chk_fail@plt>
   0x00000000000011df <+118>:	leave  
   0x00000000000011e0 <+119>:	ret  

63 final