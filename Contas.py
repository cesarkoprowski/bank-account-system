class Conta:
    # Esse já cria a conta direto
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.movimentacoes = []

    def movimentacao(self, valor, data, descricao):
        if (valor < 0) and (self.saldo + valor < 0):
            return False, "Saldo da conta insuficiente."
        
        if (self.movimentacoes and data) < (self.movimentacoes[-1]["data"]):
            return False, "Movimentações não podem ser feitas em datas retroativas."

        self.saldo += valor
        self.movimentacoes.append({
            "valor": valor,
            "data": data,
            "descricao": descricao,
            "saldo_apos": self.saldo
        })
        return True, "Movimentação bem sucedida!"
    
class Banco:
    def __init__(self):
        self.Conta = {}

    def criar_conta(self, numero):
        if numero in self.contas:
            return False, "Número de conta já existe."
        
        self.contas[numero] = ContaBancaria(numero)
        return True, "Conta aberta com sucesso!"

    def consultar_saldo(self, numero):
        if numero not in self.contas:
            return None, "Esta conta não existe."
        
        return self.contas[numero].saldo, "Consulta de saldo realizada!"