from Conta import Conta

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero):
        if numero in self.contas:
            return "Número de conta já existe."

        self.contas[numero] = Conta(numero)
        return "Conta aberta com sucesso!"

    def consultar_saldo(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."

        return f"O saldo da conta {numero} é R$ {self.contas[numero].saldo:.2f}"

    def realizar_movimentacao(self, numero, valor, data, descricao):
        if numero not in self.contas:
            return "Esta conta não existe."

        return self.contas[numero].movimentacao(valor, data, descricao)

    def extrato(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."

        extrato = self.contas[numero].movimentacoes
        if not extrato:
            return "Não há movimentações registradas na conta."

        return extrato