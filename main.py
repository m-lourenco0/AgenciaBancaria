from atendimento import Atendimento
from fila import Fila


def menu():
    print("""
    1. Gerar atendimento
    2. Controle de caixas
    3. Status dos caixas
    4. Status das filas
    5. Controle de atendimento
    6. Relatório de atendimento
    7. Sair
    """)
    return int(input("Digite a opção desejada: "))

def define_fila(tipo):
    if tipo == True:
        return fila_preferencial
    else:
        return fila_normal

def define_tipo():
    while True:
        tipo = input("Digite o tipo de atendimento: (N - Normal | P - Preferencial): ").upper()
        if tipo == 'N':
            return False
        elif tipo == 'P':
            return True
        else:
            print("Tipo inválido!")

def gerar_atendimento():
    print("\nGerando atendimento...\n")
    nome = input("Digite o nome do cliente: ")
    tipo = define_tipo()
    fila = define_fila(tipo)
    senha = fila.gerar_senha()
    atendimento = Atendimento(nome, senha, tipo)
    fila.inserir(atendimento)
    return atendimento


if __name__ == '__main__':

    print('Iniciando o sistema...')
    # Criando filas de atendimentos
    fila_normal = Fila()
    fila_preferencial = Fila(preferencial=True)

    while True:
        choice = menu()

        if choice == 1:
            gerar_atendimento()
        if choice == 4:
            print('\n---- Fila normal ----')
            fila_normal.imprimir_fila()
            print('\n--- Fila preferencial ----')
            fila_preferencial.imprimir_fila()
        if choice == 7:
            break
