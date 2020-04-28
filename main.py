import os
from Assembler import *
from memory.Memory import *

def main():
        
    print("\n" + "="*40 + " LISTA DE COMANDOS " + "="*40)
    print(" $LS                            : Lista os arquivos no diretório")
    print(" $MT <nome_do_arquivo.asm>      : Inicia o montador, realizando a conversão assembly -> hexadecimal")
    print(" $EX <nome_do_arquivo.hex>      : Executa o programa indicado")
    print(" $Q                             : Termina a execução")

    while(True):

        option = input("\n MVNSimulator $ ")

        if option == "LS":
            dir = os.listdir('./userFiles')
            print("  | Arquivo")
            print("--+---------")
            for i in range(0, len(dir)):
                print(str(i) + " | " + dir[i])

        elif option == "Q": 
            exit()

        else:
            print(" Comando invalido")

# main()