mnemonic = {
    "JP" : { "code" : "0", "size" : 2, "operand" : "address" },  # CI = OP(add)
    "JZ" : { "code" : "1", "size" : 2, "operand" : "address" },  # Se ACC == 0, CI = OP(add), se não CI = CI + 2
    "JN" : { "code" : "2", "size" : 2, "operand" : "address" },  # Se ACC  < 0, CI = OP(add), se não CI = CI + 2
    "LV" : { "code" : "3", "size" : 2, "operand" : "12bitInt" }, # ACC = OP(int)
    "+"  : { "code" : "4", "size" : 2, "operand" : "address" },  # ACC = ACC + MEM[OP]
    "-"  : { "code" : "5", "size" : 2, "operand" : "address" },  # ACC = ACC - MEM[OP]
    "*"  : { "code" : "6", "size" : 2, "operand" : "address" },  # ACC = ACC * MEM[OP]
    "/"  : { "code" : "7", "size" : 2, "operand" : "address" },  # ACC = ACC / MEM[OP]
    "LD" : { "code" : "8", "size" : 2, "operand" : "address" },  # ACC = MEM[OP]
    "MM" : { "code" : "9", "size" : 2, "operand" : "address" },  # MEM[OP] = ACC
    "SC" : { "code" : "A", "size" : 2, "operand" : "address" },  # MEM[OP, OP+1] = CI + 2, CI = OP + 2
    "RS" : { "code" : "B", "size" : 2, "operand" : "address" },  # CI = OP
    "HM" : { "code" : "C", "size" : 2, "operand" : "address" },  # Parar, CI = OP, retomar de CI
    "GD" : { "code" : "D", "size" : 2, "operand" : "null" },     # AC = input, CI = CI + 2
    "PD" : { "code" : "E", "size" : 2, "operand" : "null" },     # output AC, CI = CI + 2
    "OS" : { "code" : "F", "size" : 2, "operand" : "null" }      # Call OS, CI = CI + 2
}

pseudo = { "@", "#", "K" }