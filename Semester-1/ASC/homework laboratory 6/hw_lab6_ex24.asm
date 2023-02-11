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
    s dd 12345678h, 53812AB3h, 8973DF23h
    len equ ($ - s) / 4
    s1 times len dd 0
    four db 4

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; 24. Being given a string of doublewords, build another string of doublewords which will include only the doublewords from the given string ;which have an even number of bits with the value 1.
        mov ESI, s
        mov EDI, s1
        cld 
        mov EBX, 0
        ; we parse the string from left to right (DF = 0)
        mov ECX, len
        jecxz end
        repeat:
            lodsd
            cmp EAX, EBX
            jpe condition
                stosd
            condition:
        loop repeat
        end:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
