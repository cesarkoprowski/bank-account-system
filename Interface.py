from Controlador import Controlador

def main():
    controlador = Controlador()
    while True:
        entrada = input("FatecBank: ")
        retorno = None
        if entrada == "abrir":
            conta = input("numero da conta: ")
            retorno = controlador.criar_conta(conta)
        elif entrada == "saldo":
            conta = input("numero da conta: ")
            retorno = controlador.consultar_saldo(conta)
        elif entrada == "saque" or entrada == "deposito":
            movimentacao = input("descreva a movimentação: ")
            retorno = controlador.realizar_movimentacao(movimentacao) # está dando b.o aqui na movimentação
        elif entrada == "sair":
            break

        if retorno:
            print(retorno)

    print("Sistema Encerrado.")

if __name__ == "__main__":
    main()