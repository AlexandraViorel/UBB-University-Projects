bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global _pozitivnegativ        


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 class=code
    _pozitivnegativ:
        ; create new stack frame
        push EBP
        mov EBP, ESP
    
        mov EAX, [ESP + 8] ; we put the number in EAX
        
        cmp EAX, 0
        jge positive
        jl negative
        positive:
            mov EBX, [ESP + 12] 
            mov ECX, [ESP + 16]
            add ECX, 4
            mov [EBX + ECX], EAX
            jmp final
        negative:
            mov EBX, [ESP + 20]
            mov ECX, [ESP + 24]
            add ECX, 4
            mov [EBX + ECX], EAX
        final:
            mov ESP, EBP
            pop EBP
            ret