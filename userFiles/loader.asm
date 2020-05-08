            @   /0
START
            GD  0
            +   AUX
            MM  MSB
            GD  0
            MM  LSB
            GD  0
            MM  SIZE
LOOP
            GD  0
            JP  MSB
RTR
            LD  LSB
            +   ONE
            MM  LSB
            JZ  CARRY
RTN
            LD  SIZE
            -   ONE
            MM  SIZE
            JZ  CHECK
            JP  LOOP
CARRY
            LD  MSB
            +   ONE
            MM  MSB
            JP  RTN
CHECK
            GD  0
            JZ  OK
MSB        K  00
LSB        K  00
            JP RTR
OK          OS 00
SIZE        K  00
ONE         K  01
AUX         K  90
            #  START