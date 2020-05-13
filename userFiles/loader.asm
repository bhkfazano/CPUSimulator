            @   /0
START
            GD  0
            +   AUX
            MM  MSB
            -   AUX
            MM  CS
            GD  0
            MM  LSB
            +   CS
            MM  CS
            GD  0
            MM  SIZE
            +   CS
            MM  CS
LOOP
            GD  0
            JP  MSB
RTR
            +   CS
            MM  CS
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
            +   ONE
            JP  RTN
CHECK
            GD  0
            -   CS
            JZ  OK
MSB         K   00
LSB         K   00
            JP  RTR
OK          OS  00
SIZE        K   00
ONE         K   01
AUX         K   90
CS          K   00
            #   START