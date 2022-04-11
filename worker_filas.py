import threading
from datetime import datetime
import time
import matplotlib.pyplot as plt

def worker_fila(args):
    worker = threading.Thread(target=check_time(args))
    worker.daemon = True
    worker.start()

def check_time(filas):
    for fila in filas:
        if (len(fila.fila) > 0):
            data_inicio = fila.fila[0].data_inicio
            elapsed_time = datetime.now() - data_inicio
            if (elapsed_time.seconds > 15):
                text = f'Os atendimentos de sua fila {fila.fila[0].get_tipo} estão em espera por {elapsed_time.minute} minutos. Recomendamos abrir um novo caixa caso disponível'
                fig = plt.figure()
                ax = fig.add_subplot()
                ax.text(3, 8, 'boxed italics text in data coords', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})