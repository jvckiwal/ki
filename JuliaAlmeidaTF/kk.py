import pandas as pd 




def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Número total de servidores")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
          totalservidores = pd.read_csv("servidores_ativos.csv", usecols = ['nome'])
          print(totalservidores)

        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        

if __name__ == "__main__":
    menu_principal()

