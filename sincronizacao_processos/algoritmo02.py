
import threading
import time

# Variável compartilhada
vez = 0
ambos_na_regiao_critica = False
semaforo = threading.Semaphore(1)

# Função que será executada em uma thread
def processoA():
    global vez, ambos_na_regiao_critica
    for _ in range(2):
        print("Inicio do Processo A")
        vez = 0
        # Região crítica
        with semaforo:
            for _ in range(3):
                print("Regiao Critica de A")
            if vez == 1:
                ambos_na_regiao_critica = True
        if ambos_na_regiao_critica:
            print("AMBOS OS PROCESSOS ESTAO NA REGIAO CRITICA")
        time.sleep(1)
        vez = 1
        ambos_na_regiao_critica = False

# Outra função que será executada em outra thread
def processoB():
    global vez, ambos_na_regiao_critica
    for _ in range(2):
        print("Inicio do Processo B")
        vez = 1
        # Região crítica
        with semaforo:
            for _ in range(3):
                print("Regiao Critica de B")
            if vez == 0:
                ambos_na_regiao_critica = True
        if ambos_na_regiao_critica:
            print("AMBOS OS PROCESSOS ESTAO NA REGIAO CRITICA")
        time.sleep(1)
        vez = 0
        ambos_na_regiao_critica = False

# Criação das threads
thread1 = threading.Thread(target = processoA)
thread2 = threading.Thread(target = processoB)

# Início das threads
thread1.start()
thread2.start()

# Espera pelo término de ambas as threads
thread1.join()
thread2.join()

print("Ambas as tarefas foram concluidas")
