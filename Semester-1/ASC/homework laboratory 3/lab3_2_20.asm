bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 12h
    b dw 534h
    c dd 112233h
    d dq 887766554433h

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; a - b - (c - d) + d
        mov EBX, dword [d]
        mov ECX, dword [d + 4]
        mov EAX, [c]
        cdq
        sub EAX, EBX
        sbb EDX, ECX
        ; EDX:EAX = c - d 
        mov EBX, EAX
        mov ECX, EDX 
        ; ECX:EBX = c - d 
        mov AL, [a]
        cbw
        mov DX, [b]
        sub AX, DX 
        ; AX = a - b
        cwde
        cdq 
        ; EDX:EAX = a - b 
        sub EAX, EBX
        sbb EDX, ECX 
        ; EDX:EAX = a - b - (c - d)
        mov EBX, dword [d]
        mov ECX, dword [d + 4]
        ; ECX:EBX = d
        add EAX, EBX 
        adc EDX, ECX 
        ; EDX:EAX = a - b - (c - d) + d
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
