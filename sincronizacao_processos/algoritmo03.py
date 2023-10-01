import threading
import time

chaveA = 0 
chaveB = 0

def processoA():
    global chaveA, chaveB
    
    for _ in range(2):
        print("Inicio do Processo A")
        while chaveB !=0 :
            chaveA = 0
            print("Processo A em Espera Ocupada")
            time.sleep(1)
            chaveA = 1

        for _ in range(3):
            print("Regiao Critica de A")

        chaveA = 0

        for _ in range(3):
            print("Regiao NAO Critica de A")
            time.sleep(0.01)


def processoB():
   global chaveA, chaveB

   for _ in range(2):
        print("Inicio do Processo B")

        while chaveA != 1 :
            chaveB = 0
            print("Processo B em Espera Ocupada")
            time.sleep(0.12)
            chaveB = 1

        for _ in range(3):
            print("Regiao Critica de B")
        
        chaveB = 0
        

        for _ in range(3):
            print("Regiao NAO Critica de B")


thread1 = threading.Thread(target = processoA)
thread2 = threading.Thread(target = processoB)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluidas")