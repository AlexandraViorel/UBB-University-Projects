bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern scanf
extern fopen
extern fprintf
extern fclose
extern strlen
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import strlen msvcrt.dll
                          
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a times 20 resb 1
    
    read_format db "%s", 0
    print_format db "%s", 0
    f db "30.txt", 0
    mode db "w", 0
    f_descriptor resd 1
    dollar equ '$'
    ok db 0

; our code starts here
segment code use32 class=code
    start:
        ; 30. A file name (defined in data segment) is given. Create a file with the given name, then read words from the keyboard until character '$' is read from the keyboard. Write only the words that contain at least one digit to file.
        
        ; we will open the file 
        
        push mode
        push f
        call [fopen]
        add ESP, 4 * 2
        
        mov [f_descriptor], EAX 
        cmp EAX, 0
        je final
            back:
                ; we read a word
                push dword a
                push read_format
                call [scanf]
                add ESP, 4 * 2
                
                ; we check if the word is not the dollar sign
                mov AL, [a]
                cmp AL, dollar
                
                je final1
                    ; we put 0 in ok which will help us know if the word contains a digit or not 
                    ; if ok == 0  => the word does not have any digit
                    ; if ok == 1  => the word has at least one digit 
                    mov byte[ok], 0
                    ; we find the length of the word 
                    mov ESI, a
                    push a 
                    call [strlen]
                    add ESP, 4 * 1
                    
                    ; we put the length of the word in ECX
                    mov ECX, EAX 
                    ; we check if the word has at least one digit and if it has we will put 1 in ok
                    back2:
                        lodsb
                        cmp AL, '0'
                        jl here
                        cmp AL, '9'
                        jg here 
                        mov byte[ok], 1
                        here:
                    loop back2
                    ; if ok == 1  => we will write the word in the file 
                    cmp byte[ok], 1
                    jnz here2
                        push dword [a]
                        push print_format
                        push dword[f_descriptor]
                        call [fprintf]
                        add ESP, 4 * 3
                    here2:
                jmp back
        final:
        final1:
        
        ; we close the file 
        push dword[f_descriptor]
        call [fclose]
        add ESP, 4 * 1
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
