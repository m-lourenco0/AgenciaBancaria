from atendimento import Atendimento
from caixa import Caixa
from fila import Fila
from datetime import datetime
import ctypes
import math
import pandas as pd
import os
import time


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

def status_caixas(caixas):
    caixas_dict = {'Caixa': [], 'Status': [], 'Tipo': [], 'Atendimento': []}
    for caixa in caixas:
        caixas_dict['Caixa'].append(caixa.numero)
        caixas_dict['Status'].append(caixa.get_status())
        caixas_dict['Tipo'].append(caixa.get_tipo())
        caixas_dict['Atendimento'].append(caixa.get_status_atendimento())
    df = pd.DataFrame(caixas_dict)
    print(df.to_string())

def alterar_status(lista_caixas, num):
    caixa = lista_caixas[num-1]
    if caixa.atendimento:
        print('O caixa atual está em atendimento, não é possível alterar o status!')
    else:
        if caixa.aberto:
            caixa.fechar()
        else:
            caixa.abrir()

def check_time(filas):
    for fila in filas:
        if (len(fila.fila) > 0):
            data_inicio = fila.fila[0].data_inicio
            elapsed_time = datetime.now() - data_inicio
            minutes = elapsed_time.seconds / 60
            if (minutes > 15):
                t = f'Os atendimentos de sua fila {fila.fila[0].get_tipo()} estão em espera por aproximadamente {math.ceil(minutes)} minutos.\n\nRecomendamos abrir um novo caixa caso disponível.'
                ctypes.windll.user32.MessageBoxW(0, t, "Alerta!", 1)

def alterar_status_caixa(caixa, fila_normal, fila_preferencial):
    cx = lista_caixas[caixa-1]
    if (cx.atendimento):
        gravar_log(cx.gerar_log())
        cx.finalizar_atendimento()
    else:
        if (cx.aberto):
            if (cx.tipo):
                if (fila_preferencial.tamanho() > 0):
                    cx.atendimento = fila_preferencial.remover(0)
                else:
                    cx.atendimento = fila_normal.remover(0)
            else:
                if (fila_normal.tamanho() > 0):
                    cx.atendimento = fila_normal.remover(0)
                else:
                    cx.atendimento = fila_preferencial.remover(0)
            cx.iniciar_atendimento()
        else:
            print("O caixa atual está fechado!")


def gravar_log(log):
    df = pd.read_csv('logs.csv')
    df = df.append(log, ignore_index=True)
    df.to_csv('logs.csv', index=False)

def imprime_relatorio():
    df = pd.read_csv('logs.csv')
    print(df.to_string())
    print(f'\n\nTotal de atendimentos: {len(df)}\nTempo médio de espera: {round(df["Tempo de Atendimento (seg)"].mean(), 2)} segundos')

if __name__ == '__main__':

    print('Iniciando o sistema...')
    # Criando filas de atendimentos
    print('Criando filas...')
    fila_normal = Fila()
    fila_preferencial = Fila(preferencial=True)
    filas = [fila_normal, fila_preferencial]
    # Criando caixas (1-5 NORMAL | 6-7 PREFERENCIAL)
    print('Criando caixas...')
    caixa_normal_1 = Caixa(1)
    caixa_normal_2 = Caixa(2)
    caixa_normal_3 = Caixa(3)
    caixa_normal_4 = Caixa(4)
    caixa_normal_5 = Caixa(5)
    caixa_preferencial_6 = Caixa(6, True)
    caixa_preferencial_7 = Caixa(7, True)
    lista_caixas = [caixa_normal_1, caixa_normal_2, caixa_normal_3, caixa_normal_4, caixa_normal_5, caixa_preferencial_6, caixa_preferencial_7]

    # Abrindo primeiros caixas 1 e 6
    caixa_normal_1.aberto = True
    caixa_preferencial_6.aberto = True

    while True:
        check_time(filas)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        choice = menu()
        if choice == 1:
            at = gerar_atendimento()
            print(f'\nAtendimento {at.get_tipo()} gerado: {at.nome} - {at.senha}')
            time.sleep(2)
        if choice == 2:
            print("\nControle de caixas:")
            status_caixas(lista_caixas)
            caixa = int(input("\nDigite o número do caixa para abrir ou fechar: "))
            alterar_status(lista_caixas, caixa)
            time.sleep(3)
        if choice == 3:
            print("\nStatus dos caixas:\n")
            status_caixas(lista_caixas)
            input('\nPressione ENTER para continuar...')
        if choice == 4:
            print('\n---- Fila normal ----')
            fila_normal.imprimir_fila()
            print('\n--- Fila preferencial ----')
            fila_preferencial.imprimir_fila()
            input('\nPressione ENTER para continuar...')
        if choice == 5:
            print("\nControle de atendimento\n")
            status_caixas(lista_caixas)
            caixa = int(input("\nDigite o número do caixa que deseja alterar o atendimento: "))
            alterar_status_caixa(caixa, fila_normal, fila_preferencial)
        if choice == 6:
            print("\nRelatório de atendimento\n")
            imprime_relatorio()
            input('\nPressione ENTER para continuar...')
        if choice == 7:
            break
