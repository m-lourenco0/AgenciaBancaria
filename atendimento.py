from datetime import datetime
from fila import Fila

class Atendimento:
    def __init__(self, nome, senha, preferencial=False):
        self.nome = nome
        self.senha = senha
        self.atendimento = False
        self.preferencial = preferencial
        self.data_inicio = datetime.now()
        self.data_fim = None

    def atender(self):
        self.atendimento = True

    def finalizar(self):
        self.atendimento = False

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def imprime_dados(self):
        tipo = 'Preferencial' if self.preferencial else 'Normal'
        print(f'Senha: {self.senha}\nNome: {self.nome}\nTipo: {tipo}\nData chegada: {self.data_inicio}\n')