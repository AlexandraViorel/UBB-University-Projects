bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern scanf
extern fopen
extern fprintf
extern fclose
extern maxim 

import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import fopen msvcrt.dll 
import fprintf msvcrt.dll
import fclose msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; 
    a resd 1
    b resd 1
    read_format db "%d", 0 ; signed numbers in base 10
    print_format db "%x", 0 ; numbers in base 16
    file db "max.txt", 0
    mode db "w", 0
    file_descriptor resd 1
    

; our code starts here
segment code use32 class=code
    start:
        ; 24. Read a string of signed numbers in base 10 from keyboard. Determine the maximum value of the string and write it in the file max.txt (it will be created) in 16  base.
        
        ; We will read words from the keyboard until the digit '0' is read from the keyboard
        
        ; if the first number read is 0, we will consider it the greatest number read 
        
        ; we will store the greatest number in the address of b
        
        ; we will read the first number and store it in the address of b because it is the greatest number read
        
        push b 
        push read_format 
        call [scanf]
        add ESP, 4 * 2
        
        mov ECX, [b] ; we use ECX to see if the number read is 0
        jecxz endfor
            repeta:
                ; we will read the rest of the numbers and store them in the address of a
                push a 
                push read_format
                call [scanf]
                add ESP, 4 * 2
                
                mov ECX, [a] ; we will use ECX to see if the last number read is 0
                jecxz endf ; if the last number read is 0 we will not consider it the greatest number
                
                ; we push on the stack the numbers we will use in the module
                push dword [a]
                push dword [b]
                call maxim

                mov dword [b], EAX ; we store the greatest number in the address of b    
            loop repeta
          endf:
        endfor:
        
        ; we create and open the file for writing
        push mode
        push file
        call [fopen]
        add ESP, 4 * 2
        
        mov [file_descriptor], EAX
        cmp EAX, 0
        je final
            ; we write the greatest number read in the file
            push dword [b]
            push print_format
            push dword [file_descriptor]
            call [fprintf]
            add ESP, 4 * 3
        final:
        
        ; we close the file
        push dword [file_descriptor]
        call [fclose]
        add ESP, 4 * 1
        

    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
