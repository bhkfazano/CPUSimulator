      @    /100
START LD   COMP
      MM   CONT
IN    LD  LDA0
      MM   LDA
      LD  LDA0+1
      MM   LDA+1
LDA   LD  INIC
      PD   SAIDA 
      LD  CONT
      -    UM
      MM   CONT
      JZ   FORA 
      LD  LDA+1
      +    UM  
      MM   LDA+1
      JZ   INCR 
      JP   LDA  
INCR  LD  LDA    
      +    UM     
      MM   LDA
      JP   LDA
FORA  HM   START
      @   /200
UM    K   1      
CONT  K   0       
LDA0  LD INIC
      @   /F00    
COMP  K   5      
INIC  K   01
      K   02
      K   03
      K   04
      K   05