          global    _start

          section   .text
_start:   mov       rax, 1                 
          mov       rdi, 1           
          mov       rsi, welcome_message    
          mov       rdx, 25               
          syscall
          mov       rax,0
          mov       rdi,0
          mov       rsi,message
          mov       rdx,50
          syscall
          mov       rax,15
          syscall                    

          section   .data
welcome_message:  db        "Signal, signal everywhere", 50 
message   db            "\n"
binsh     db            "/bin/sh"

