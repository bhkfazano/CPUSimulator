INIC    @    /445
CONV    
        JP   MSBN
RTN     +    30
        LD   COUNT
        -    01
        JZ   CODE
        LD   LSBN
        +    01
        JP   CONV
CODE       #parei aqui 
CTES    @    /600
NUSP
        K    00
        K    09
        K    08
        K    03
        K    05
        K    03
        K    04
        K    05
CODIGO  
        K    00
        K    00
        K    00
        K    00
        K    00
        K    00
        K    00
        K    00
COUNT   K    08
MSBN    K    96
LSBN    K    00
        JP   RTN