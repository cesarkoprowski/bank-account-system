from Contas import Contas
from Contas import formata_data

def compara_data(movimentacoes, data):
    data = formata_data(data)
    for i in range(len(movimentacoes)):
        if movimentacoes[i]["data"] >= data:
            return i
            
    return -1 

class Controlador:
    def __init__(self):
        self.contas = {}

    def abrir_conta(self, numero):
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

    def extrato(self, numero, data):
        if numero not in self.contas:
            return "Esta conta não existe."

        movimentacoes = self.contas[numero].movimentacoes
        indice = compara_data(movimentacoes, data)

        texto = ""

        print(f"Indice = {indice}")

        if not movimentacoes:
            return "Não há movimentações registradas na conta"
        
        if indice == -1:
            return "Não há movimentações registradas na conta"
        else:
            for i in range(indice, len(movimentacoes)):
                texto += (
                    "--------------------------------------------------------------\n"
                    f"{movimentacoes[i]['movimento']} de valor R$ {movimentacoes[i]['valor']:.2f} realizado em {movimentacoes[i]['data'][2]}/{movimentacoes[i]['data'][1]}/{movimentacoes[i]['data'][0]}\n"
                    f"Descrição adicional: {movimentacoes[i]['descricao']}\n"
                    f"Saldo após a movimentação: R$ {movimentacoes[i]['saldo_apos']:.2f}\n"
                    "--------------------------------------------------------------\n"
                )

                

        return texto
    
    def fechar_conta(self, numero):
        if numero not in self.contas:
            return "Esta conta não existe."
        
        if self.contas[numero].saldo == 0:
            del self.contas[numero]
            return "Conta fechada com sucesso"
        else:
            return f"A conta não pode ser fechada"