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
    s1 db 1, 3, 6, 2, 3, 2
    l1 equ $ - s1
    s2 db 6, 3, 8, 1, 2, 5
    d times l1 db 0 ; we reserve l1 bytes for the destination string and initialize it with 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;Two byte strings S1 and S2 of the same length are given. Obtain the string D where 
        ;each element is the difference of the corresponding elements from S1 and S2
        
        mov ECX, l1 ; we put the length l1 in ECX in order to make the loop
        ; Remark: the length of the strings s1 and s2 are the same, so we only calculate and use one of it
        mov ESI, 0
        jecxz endFor
        Repeat:
            mov AL, [s1 + ESI]
            mov BL, [s2 + ESI]
            sub AL, BL
            mov [d + ESI], AL
            inc ESI
        loop Repeat
        endFor:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
