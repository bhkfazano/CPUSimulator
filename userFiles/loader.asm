            @   /0
START
            GD  0
            +   AUX
            MM  POS1
            GD  0
            MM  POS2
            GD  0
            MM  SIZE
LOOP
            GD  0
            JP  POS1
RTR
            LD  POS2
            +   ONE
            MM  POS2
            JZ  CARRY
RTN
            LD  SIZE
            -   ONE
            MM  SIZE
            JZ  CHECK
            JP  LOOP
CARRY
            LD  POS1
            +   ONE
            MM  POS1
            +   ONE
            JP  RTN
CHECK
            GD  0
            JZ  OK
OK
POS1        K  00
POS2        K  00
            JP RTR
SIZE        K  00
ONE         K  01
AUX         K  90
            #  START