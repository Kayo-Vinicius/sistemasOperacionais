import threading
import time

# Função que será executada em uma thread
def task1():
    print("Início da Tarefa 1")
    for _ in range(5):
        print("Tarefa 1 executando")
        #time.sleep(1)
    print("Fim da Tarefa 1")

# Outra função que será executada em outra thread
def task2():
    print("Início da Tarefa 2")
    for _ in range(5):
        print("Tarefa 2 executando")
        #time.sleep(0.8)
    print("Fim da Tarefa 2")

# Criação das threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Início das threads
thread1.start()
thread2.start()

# Espera pelo término de ambas as threads
thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")