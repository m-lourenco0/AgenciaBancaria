class Fila:
    def __init__(self, preferencial=False):
        self.fila = []
        self.preferencial = preferencial
        self.senha = 0

    def inserir(self, elemento):
        self.fila.append(elemento)

    def remover(self, elemento):
        return self.fila.pop(elemento)

    def tamanho(self):
        return len(self.fila)

    def gerar_senha(self):
        self.senha += 1
        return self.senha

    def imprimir_fila(self):
        for i in self.fila:
            print(f'\nPosição: {self.fila.index(i) + 1}')
            i.imprime_dados()