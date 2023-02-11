bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern fopen
extern fclose
extern fscanf
extern fprintf
extern strlen
extern fread
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll     
import strlen msvcrt.dll 
import fread msvcrt.dll                    
                       

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; 
    input_file db "input.txt", 0
    output_file db "output.txt", 0
    read_mode db "r", 0
    write_mode db "a", 0
    file_descriptor_input resd 1
    file_descriptor_output resd 1
    len equ 100
    caracter db 0
    cuvant times len db 0
    propozitie times len db 0
    lungimea_propozitiei dd 0
    contor_propozitie dd 0
    write_format db "%s", 10, 0
    read_format db "%s", 10, 0
    endfile dd 0

; our code starts here
segment code use32 class=code
    start:
        ; Scrieti un program care citeste dintr un fisier propozitii (propozitiile sunt siruri de caractere care se termina cu .). Scrieti in alt fisier
        ; doar propozitiile de ordin par. Numele celor doua fisiere se dau in segmentul de date.
        
        ; avem un contor pt a numerota propozitiile, care incepe de la 1
        
        ; deschidem fisierul din care citim
        push dword read_mode
        push input_file
        call [fopen]
        add ESP, 4*2
        
        ; verificam daca nu a aparut o eroare la deschidere
        mov dword [file_descriptor_input], EAX
        cmp EAX, 0 
        je final
        
            my_loop:
            ; deschidem fisierul in care scriem
            push dword write_mode
            push output_file
            call [fopen]
            add ESP, 4*2
            
            ; verificam daca nu a aparut o eroare la deschidere 
            mov dword [file_descriptor_output], EAX
            cmp EAX, 0
            je final1
            
            mov EDI, dword propozitie
        
            ; citim o propozitie pana la punct, caracter cu caracter
            another_loop:
            
            push dword [file_descriptor_input]
            push 1
            push 1
            push dword caracter
            call [fread]
            add ESP, 4*3
            
            mov ECX, 1
            mov ESI, dword caracter
            loop1:
            
            mov EAX, 0
            movsb
            mov AL, byte [caracter]
            cmp AL, "."
            je am_ajuns_la_punct
            
            
            loop loop1
            
            
            ; verificam daca nu am ajuns la sfarsitul fisierului (singurul mod in care putem iesi din loop)
            ;cmp EAX, -1
            ;je end_of_file
            
            ; aflam lungimea propozitiei (va fi in EAX)
            ;push dword cuvant
            ;call [strlen]
            ;add ESP, 4*1
            
            ;add dword [lungimea_propozitiei], EAX
            
            ; vedem daca am ajuns la punct
            ;mov ECX, EAX
            ;cld
            ;mov ESI, dword cuvant
            ;loop1:
            
            ;lodsb 
            ;scasb
            ;cmp AL, "."
            ;je am_ajuns_la_punct
            
            ;loop loop1
            
            
            
            jmp another_loop
            
            am_ajuns_la_punct:
            
            ; marim contorul 
            inc dword [contor_propozitie]
            
            ;verificam daca propozitia este de ordin par
            mov AX, word [contor_propozitie]
            mov DX, word [contor_propozitie + 2]
            mov BX, 2
            div BX
            cmp DX, 0
            je este_par
                jmp nu_este_par
            este_par:
            
                ; daca propozitia este de ordin par o scriem in fisier
                push dword propozitie
                push write_format
                push dword [file_descriptor_output]
                call [fprintf]
                add ESP, 4*3
            nu_este_par:
            
            ;mov ECX, dword [len]
            ;mov EDI, propozitie
            ;mov EAX, 0
            ;loop3:
                
            ;    movsb
            
            ;loop loop3
            ;mov dword [lungimea_propozitiei], 0
                
            jmp my_loop
            
        end_of_file:
        final:
        final1:
        
        ; inchidem fisierul din care am citit
        push dword [file_descriptor_input]
        call [fclose]
        add ESP, 4*1
        
        ; inchidem fisierul in care am scris
        push dword [file_descriptor_output]
        call [fclose]
        add ESP, 4*1
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
