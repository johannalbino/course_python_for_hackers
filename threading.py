import threading
import time


def faz_algo(i):
    print(f'Executando thread {i}....')
    time.sleep(3)
    print(f'Finalizando a thread {i}....')


for i in range(5):
    t = threading.Thread(target=faz_algo, args=(i,))
    t.start()