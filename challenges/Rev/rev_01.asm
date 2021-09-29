   0x000011d1 <+4>:	push   ebp
   0x000011d2 <+5>:	mov    ebp,esp
   0x000011d4 <+7>:	sub    esp,0x10
   0x000011dc <+15>:	add    eax,0x2dfc
   0x000011e1 <+20>:	mov    edx,DWORD PTR [ebp+0x8]
   0x000011e4 <+23>:	mov    eax,DWORD PTR [ebp+0xc]
   0x000011e7 <+26>:	add    eax,edx
   0x000011e9 <+28>:	mov    DWORD PTR [ebp-0x8],eax
   0x000011ec <+31>:	mov    eax,DWORD PTR [ebp+0x8]
   0x000011ef <+34>:	imul   eax,DWORD PTR [ebp+0xc]
   0x000011f3 <+38>:	lea    edx,[eax+0xa]
   0x000011f6 <+41>:	mov    eax,DWORD PTR [ebp-0x8]
   0x000011f9 <+44>:	imul   eax,edx
   0x000011fc <+47>:	mov    DWORD PTR [ebp-0x4],eax
   0x000011ff <+50>:	mov    eax,DWORD PTR [ebp-0x4]
   0x00001202 <+53>:	leave  
   0x00001203 <+54>:	ret    

args 15,25
ans 15400