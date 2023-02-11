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
    b db 13h
    c db 06h
    e dw 150h
    f dw 234h
    g dw 145h
    a1 db 3h
    a2 db 5h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; [(e+f-g)+(b+c)*3]/5
        mov BX, [e] ; BX = e
        add BX, [f] ; BX = e + f
        sub BX, [g] ; BX = e + f - g
        mov AL, [b] ; AL = b
        add AL, [c] ; AL = b + c
        mul byte[a1] ; AX = (b + c)*3
        add AX, BX  ; AX = (b + c)*3 + (e + f - g)
        div byte[a2] ; AX = [(b + c)*3 + (e + f - g)]/5
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
