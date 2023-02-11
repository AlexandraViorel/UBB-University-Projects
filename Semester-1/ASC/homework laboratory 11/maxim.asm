bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global maxim        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 public code
    maxim:
        ; ...
        mov EDX, [ESP + 4] ; in EDX we will store the greatest number read until now
        mov EBX, [ESP + 8] ; in EBX we will store the last number read
        cmp EBX, EDX ; we compare the numbers in order to see which one is greater
        jl lower
            mov EAX, EBX ; if EBX > EDX we will put the number from EBX in the address of b 
        lower: 
        jg greater
            mov EAX, EDX
        greater:
        
        ret 4 * 2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
