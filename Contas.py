from datetime import datetime

class Contas:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.movimentacoes = []

    def movimentacao(self, valor, data, descricao):
        saque = valor < 0

        if valor == 0:
            return "Não e possível realizar movimentação de R$ 0,00"

        if saque and (self.saldo + valor < 0):
            return "Saldo insuficiente"

        data_formatada = utils.formata_data(data)
        if not data_formatada:
            return "Data inválida"

        if self.movimentacoes and data < self.movimentacoes[-1]["data"]:
            return "Movimentação tem data retroativa"

        self.saldo += valor
        self.movimentacoes.append({
            "valor": valor,
            "data": data_formatada,
            "descricao": descricao,
            "saldo_apos": self.saldo
        })

        if saque:
            return "Saque realizado com sucesso"

        return "Depósito realizado com sucesso"
    
    def formata_data(data_str):
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            data_formatada = (data.year, data.month, data.day)
            return data_formatada
        except ValueError:
            return None
