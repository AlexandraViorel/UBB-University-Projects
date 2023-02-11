bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern scanf
extern printf

import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a resd 1
    b resd 1
    read_format db "%d", 0
    print_format db "The smallest number read is %d", 13, 0
    

; our code starts here
segment code use32 class=code
    start:
        ; 30. Read numbers (in base 10) in a loop until the digit '0' is read from the keyboard. Determine and display the smallest number from those that have been read.
        
        ; we will store the smallest number in the address of b
        
        ; we will read the first number and store it in the address of b because it is the smallest number read
        push b 
        push read_format
        call [scanf]
        add ESP, 4 * 2
        
        mov ECX, [b] ; we use ECX to see if the number read is 0
        jecxz endfor
            repeta 
                ; we will read the rest of the numbers and store them in the address of a
                push a
                push read_format
                call [scanf]
                add ESP, 4 * 2
                
                mov EDX, [b] ; in EDX we will store the smallest number read until now 
                mov EBX, [a] ; in EBX we will store the last number read
                mov ECX, [a] ; we will use ECX to see if the last number read is 0
                jecxz endf   ; if the last number read is 0 we will not consider it the smallest number

                cmp EBX, EDX ; we compare the numbers in order to see which one is smaller
                    jg greater   
                        mov dword [b], EBX   ; if EBX < EDX we will put the number from EBX in the adress b 
                    greater:
            loop repeta
          endf
        endfor
                
        push dword [b] 
        push print_format
        call [printf]
        add ESP, 4 * 2
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
