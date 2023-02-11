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
    a dw 100h
    b db 43h
    e dd 112233h
    x dq 887766554433h
    a1 db 02h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; x - b + 8 + (2 * a - b) / (b * b) + e
        ; signed
        mov BX, [a]
        mov AL, [a1]
        cbw
        mul BX 
        ; AX = 2 * a 
        mov BX, AX
        ; BX = 2 * a
        mov AL, [b]
        cbw
        ; AX = b 
        sub BX, AX 
        ; BX = 2 * a - b
        mov AL, [b]
        imul byte [b]
        ; AX = b * b
        mov CX, AX 
        ; CX = b * b
        mov AX, BX
        ; AX = 2 * a - b
        idiv word CX 
        ; AX = (2 * a - b) / (b * b)
        cwde
        add EAX, [e]
        add EAX, 8h
        ; EAX = (2 * a - b) / (b * b) + e + 8h
        mov EBX, EAX 
        mov AL, [b]
        cbw 
        cwde 
        ; converts b from byte to doubleword 
        sub EBX, EAX
        ; EBX = (2 * a - b) / (b * b) + e + 8h - b
        mov EAX, EBX 
        cdq
        ; converts dword to qword
        ; EDX:EAX = (2 * a - b) / (b * b) + e + 8h - b
        mov EBX, dword [x]
        mov ECX, dword [x + 4]
        add EAX, EBX 
        adc EDX, ECX 
        ; EDX:EAX = x + (2 * a - b) / (b * b) + e + 8h - b
        
   
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
