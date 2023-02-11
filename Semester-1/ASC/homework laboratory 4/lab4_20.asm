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
                                        
    a dw 0111010110100101b
    b dw 1001110001111011b
    c dd 0 ; the result is: 00000000000000001010110110110100b
    d dw c 

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;Given the words A and B, compute the doubleword C as follows:
        ;   - the bits 0-5 of C are the same as the bits 3-8 of A
        ;   - the bits 6-8 of C are the same as the bits 2-4 of B
        ;   - the bits 9-15 of C are the same as the bits 6-12 of A
        ;   - the bits 16-31 of C have the value 0

        mov EBX, 0 ; we will compute the result in EBX
        
        ; we isolate bits 3-8 of a
        mov EAX, 0
        mov AX, word [a]
        and AX, 0000000111111000b
        
        ; we shift 3 positions to right
        mov CL, 3
        shr AX, CL
        
        ; we put the bits into the result
        or EBX, EAX 
        
        ; we isolate bits 2-4 of b
        mov EAX, 0
        mov AX, word [b]
        and AX, 0000000000011100b
        
        ; we shift 4 positions to left
        mov CL, 4
        shl AX, CL

        ; we put the bits into the result 
        or EBX, EAX
        
        ; we isolate bits 6-12 of a 
        mov EAX, 0
        mov AX, word [a]
                      ;111111111
        and AX, 0001111111000000b
        
        ; we shift 3 positions to left 
        mov CL, 3
        shl AX, CL
        
        ; we put the bits into the result
        or EBX, EAX
        
        ; we force the value of bits 16-31 of the result to the value 0
        and EBX, 00000000000000001111111111111111b
        
        ; we move the result from the register to the variable 
        mov [c], EBX
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
