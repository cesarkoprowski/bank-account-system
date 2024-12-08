from Controlador import Controlador

def main():
    controlador = Controlador()
    while True:
        entrada = input("FatecBank: ")
        retorno = None
        if entrada == "abrir":
            conta = input("Numero da conta: ")
            retorno = controlador.abrir_conta(conta)
        elif entrada == "saldo":
            conta = input("Numero da conta: ")
            retorno = controlador.consultar_saldo(conta)
        elif entrada == "sacar":
            movimentacao = input("Descreva a movimentação: ")
            retorno = controlador.realizar_movimentacao(movimentacao, "Saque")
        elif entrada == "depositar":
            movimentacao = input("Descreva a movimentação: ")
            retorno = controlador.realizar_movimentacao(movimentacao, "Deposito")
        elif entrada == "extrato":
            conta, data = input("Insira conta e a data inicial: ").split(' ')            
            retorno = controlador.extrato(conta, data)
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