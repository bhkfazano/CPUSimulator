import os
from MVNSimulator import *

def main():

    simulator = MVNSimulator()
    simulator.start()

    objectCode = []
        
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

        elif len(option.split()) == 2 and option.split()[0] == "MT":
            
            path = './userFiles/' + option.split()[1]
            simulator.assemble(path)

        elif  len(option.split()) == 2 and option.split()[0] == "EX":

            path = option.split()[1]
            simulator.run(path)


        elif option == "Q": 
            exit()

        else:
            print(" Comando invalido")

main()