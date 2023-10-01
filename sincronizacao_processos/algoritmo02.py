import threading
import time

vez = 0  # trava

#Função que será executada em uma thread
def processoA():
    global vez
    for _ in range(2):
        print("Inicio do Processo A")
        while vez != 0:
            print("Processo A em Espera Ocupada")
        vez = 1  #Mudando o valor da variavel vez antes de entrar na região crítica

        #regiao critica
        for _ in range(3):
            print("Regiao Critica de A")
            # time.sleep(1)

        vez = 0 #Mudando o valor da variavel vez depois de sair da região crítica
        

        # Região não crítica
        for _ in range(3):
            print("Regiao NAO Critica de A")
            time.sleep(1)

def processoB():
    global vez
    for _ in range(2):
        print("Inicio do Processo B")
        while vez != 1:
            print("Processo B em Espera Ocupada")
        vez = 0   #Mudando o valor da variavel vez antes de entrar na região crítica

        #regiao critica
        for _ in range(3):
            print("Regiao Critica de B")
            time.sleep(1)

        vez = 1 #Mudando o valor da variavel vez depois de sair da região crítica

        #regiao nao critica
        for _ in range(3):
            print("Regiao NAO Critica de B")
            time.sleep(1)

#Criação das threads
thread1 = threading.Thread(target=processoA)
thread2 = threading.Thread(target=processoB)

#Início das threads
thread1.start()
thread2.start()

#Espera pelo término de ambas as threads
thread1.join()
thread2.join()

print("Ambas as tarefas foram concluidas")
