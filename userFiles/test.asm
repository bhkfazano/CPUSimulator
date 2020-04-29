            @       /0100
INIC        LD      UM
            LV      0012
            MM      /0112
            MM      IMPAR
            MM      N2
LOOP        LD      /0010
            -       N
            JZ      FORA
             LD     CONT
            +       UM
            MM      CONT
            LD      IMPAR
            +       DOIS
            MM      IMPAR
            +       N2
            MM      N2
            JP      LOOP
FORA        LD      N2
            OS      /0000
            @       /0200
UM          K       01
DOIS        K       02
IMPAR       K       00
N           K       04
N2          K       00
CONT        K       00
            #       INIC