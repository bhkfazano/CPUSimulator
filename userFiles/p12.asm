        @    /445
CODE    HM   ST
ST      JP   LDN3
R3      +    AUX
        MM   AUX
        /    SIXT
        JZ   G1
        *    SIXT
        MM   AUX2
        LD   AUX
        -    AUX2
        JP   G2
        MM   AUX
G1      LD   AUX
G2      JP   MMC1
R4      LD   COUNT
        -    ONE
        MM   COUNT
        JZ   SAVE
        LD   LDN2
        -    ONE
        MM   LDN2
        LD   MMC0
        -    ONE
        MM   MMC0
        JP   ST
SAVE    HM   GO
GO      LD   COUNT
        +    EIGHT
        MM   COUNT
RR      JP   LDC1
R5      -    TEN
        JN   G3
        +    TEN
        +    SUM2
        JP   G4
G3      +    TEN
        +    SUM1
G4      PD   00
        LD   COUNT
        -    ONE
        MM   COUNT
        JZ   OK
        LD   LDC0
        +    ONE
        MM   LDC0
        JP   RR
OK      OS   0000
        @    /600
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
LDN1    K    86
LDN0    K    00
LDN3    K    86
LDN2    K    07
        JP   R3
MMC1    K    96
MMC0    K    0F
        JP   R4
LDC1    K    86
LDC0    K    08
        JP   R5
AUX     K    00
AUX2    K    00
THIRTY  K    30
ONE     K    01
EIGHT   K    08
SIXT    K    10
TEN     K    0A
SUM1    K    30
SUM2    K    37
COUNT   K    08
        #    