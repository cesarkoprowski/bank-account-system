import Controlador
import Contas

def main():
    banco = Controlador
    while True:
        entrada = input("FatecBank: ")
        if entrada == "abrir":
            numero_conta = input("Digite o numero da conta que deseja abrir: ")
            banco.criar
        elif entrada == "saldo":

        elif entrada == "saque":

        elif entrada == "deposito":

        elif entrada == "sair":


    print("Sistema Encerrado.")

if __name__ == "__main__":
    main()