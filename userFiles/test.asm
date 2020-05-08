            @       /0100
INIC        LD      UM
            +       UM
            *       TRES
            MM      0300
LOOP        LD      0300
            -       UM
            MM      0300
            JZ      FORA
            JP      LOOP
FORA        
            OS      /0000
            @       /0200
UM          K       01
DOIS        K       02
IMPAR       K       11
N           K       04
TRES        K       03
CONT        K       00
            #       INIC