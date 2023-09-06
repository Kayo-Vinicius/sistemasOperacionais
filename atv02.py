import threading
import time

# Variável de controle para verificar se o tempo limite foi atingido
tempoLimite = False

# Função que será executada em uma thread
def task1():
    global tempoLimite
    print("Inicio da Tarefa 1")
    for _ in range(5):
        # Verifica se o tempo limite foi atingido
        if tempoLimite:
            print("A Tarefa 1 foi interrompida devido ao tempo limite")
            return
        print("Tarefa 1 executando")
        time.sleep(0.8)
    print("Fim da Tarefa 1")

# Outra função que será executada em outra thread
def task2():
    global tempoLimite
    print("Inicio da Tarefa 2")
    for _ in range(5):
        # Verifica se o tempo limite foi atingido
        if tempoLimite:
            print("A Tarefa 2 foi interrompida devido ao tempo limite")
            return
        print("Tarefa 2 executando")
        time.sleep(3)
    print("Fim da Tarefa 2")

# Criação das threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Início da thread1
thread1.start()

# Tempo limite da tarefa 1
thread1.join(10)

# Verifica se a thread1 foi concluída
if thread1.is_alive():
    tempoLimite = True
    print("A Tarefa 1 não foi concluída dentro do tempo limite")
else:
    # Início da thread2 após a conclusão da thread1
    thread2.start()

    # Tempo limite da tarefa 2
    thread2.join(10)

    # Verifica se a thread2 foi concluída
    if thread2.is_alive():
        tempoLimite = True
        print("A Tarefa 2 nao foi concluida dentro do tempo limite")
    else:
        print("Ambas as tarefas foram concluidas")
