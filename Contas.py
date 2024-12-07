class Conta:
    # Esse já cria a conta direto
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.movimentacoes = []

    def _formata_data(self, data_str):
        dia, mes, ano = map(int, data_str.split('/'))
        data_formatada = (ano, mes, dia)
        return data_formatada

    def movimentacao(self, valor, data, descricao):
        saque = valor < 0

        if valor == 0:
            return False, "Não e possível realizar movimentação de R$ 0,00"

        if saque and (self.saldo + valor < 0):
            return False, "Saldo insuficiente"

        if self.movimentacoes and data < self.movimentacoes[-1]["data"]:
            return False, "Movimentação tem data retroativa"

        self.saldo += valor
        self.movimentacoes.append({
            "valor": valor,
            "data": self._formata_data(data),
            "descricao": descricao,
            "saldo_apos": self.saldo
        })

        if saque:
            return True, "Saque realizado com sucesso"

        return True, "Depósito realizado com sucesso"

class Banco:
    def __init__(self):
        self.Conta = {}

    def criar_conta(self, numero):
        if numero in self.contas:
            return False, "Número de conta já existe"
        
        self.contas[numero] = ContaBancaria(numero)
        return True, "Conta aberta com sucesso!"

    def consultar_saldo(self, numero):
        if numero not in self.contas:
            return None, "Esta conta não existe."
        
        return "O saldo da conta é R$ " , self.contas[numero].saldo