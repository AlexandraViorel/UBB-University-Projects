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
    a db 15h
    b dw 345h
    c dd 112233h
    d dq 4455667788h

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;(a + c) - b + a + (d - c)
        mov EAX, dword [d]
        mov EDX, dword [d + 4] 
        mov EBX, [c]
        mov ECX, 0 
        sub EAX, EBX
        sbb EDX, ECX
        ; EDX:EAX = d - c
        mov EBX, EAX
        mov ECX, EDX
        ; ECX:EBX = d - c
        mov DX, 0
        mov AX, 0
        mov AL, [a]
        add AX, word [c]
        adc DX, word [c + 2]
        push DX
        push AX
        pop EAX
        ; EAX = a + c
        sub AX, word [b]
        add AL, byte [a]
        ; EAX = (a + c) - b + a 
        mov EDX, 0
        add EBX, EAX
        adc ECX, EDX 
        ; ECX:EBX = (d - c) + (a + c) - b + a
        mov EAX, EBX
        mov EDX, ECX 
        ; EDX:EAX = (d - c) + (a + c) - b + a
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
