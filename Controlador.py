from Contas import Contas

class Controlador:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero):
        if numero in self.contas:
            return "Número de conta já existe."

        self.contas[numero] = Contas(numero)
        return "Conta aberta com sucesso!"

    def consultar_saldo(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."

        return f"O saldo da conta {numero} é R$ {self.contas[numero].saldo:.2f}"

    def realizar_movimentacao(self, movimentacao, movimento):
        partes = movimentacao.split(' ')
        conta = partes[0]
        valor = float(partes[1])
        data = partes[2]
        descricao = " ".join(partes[3:])

        if conta not in self.contas:
            return "Esta conta não existe."

        return self.contas[conta].movimentacao(movimento, valor, data, descricao)

    def extrato(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."

        extrato = self.contas[numero].movimentacoes
        if not extrato:
            return "Não há movimentações registradas na conta."

        return extrato
    
    def fechar_conta(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."
        
        if self.contas[numero].saldo == 0:
            del self.contas[numero]
            return "Conta fechada com sucesso"
        else:
            return f"A conta não pode ser fechada"