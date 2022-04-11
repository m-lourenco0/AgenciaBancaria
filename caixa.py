from datetime import datetime

class Caixa:
    def __init__(self, numero, tipo=False):
        self.tipo = tipo # True = Preferencial | False = Normal
        self.atendimento = None
        self.aberto = False
        self.numero = numero

    def iniciar_atendimento(self):
        self.atendimento.set_caixa(self.numero)
        self.atendimento.data_fim = datetime.now()
        self.atendimento.em_andamento = True

    def finalizar_atendimento(self):
        self.atendimento.em_andamento = False
        self.atendimento = None

    def abrir(self):
        if (self.aberto):
            print("Caixa já está aberto!")
        else:
            self.aberto = True
            print("Caixa aberto!")

    def get_tipo(self):
        return 'Preferencial' if self.tipo else 'Normal'

    def get_status(self):
        return 'Aberto' if self.aberto else 'Fechado'

    def get_status_atendimento(self):
        return 'Em atendimento' if self.atendimento else 'Livre'

    def fechar(self):
        self.aberto = False

    def gerar_log(self):
        log_dict = {
            'Nome Cliente': self.atendimento.nome,
            'Tipo': self.atendimento.get_tipo(),
            'Senha': self.atendimento.get_senha(),
            'Caixa': self.atendimento.caixa,
            'Dia Atendimento': self.atendimento.data_inicio.date(),
            'Hora Chegada': self.atendimento.data_inicio.time(),
            'Hora Saída': self.atendimento.data_fim.time(),
            'Tempo de Atendimento (seg)': (self.atendimento.data_fim - self.atendimento.data_inicio).seconds
        }
        return log_dict


