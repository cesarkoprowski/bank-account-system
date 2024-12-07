from Controlador import Controlador

def main():
    controlador = Controlador()
    while True:
        entrada = input("FatecBank: ")
        retorno = None
        if entrada == "abrir":
            conta = input("Numero da conta: ")
            retorno = controlador.criar_conta(conta)
        elif entrada == "saldo":
            conta = input("Numero da conta: ")
            retorno = controlador.consultar_saldo(conta)
        elif entrada == "sacar" or entrada == "depositar":
            movimentacao = input("Descreva a movimentação: ")
            retorno = controlador.realizar_movimentacao(movimentacao) # está dando b.o aqui na movimentação
        elif entrada == "fechar":
            conta = input("Numero da conta: ")
            retorno = controlador.fechar_conta(conta)
        elif entrada == "sair":
            break

        if retorno:
            print(retorno)

    print("Sistema Encerrado.")

if __name__ == "__main__":
    main()