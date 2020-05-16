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
FORA  HM   END
      @   /200
UM    K   1      
CONT  K   0       
LDA0  LD INIC
      @   /F00    
COMP  K   10      
INIC  K   42
      K   52
      K   55
      K   4e
      K   4f
      K   48
      K   45
      K   4e
      K   52
      K   49
      K   51
      K   55
      K   45
      K   4b
      K   4f
      K   47
END   OS  00
      #   START