"""
    Implemente um programa que use 2 threads para calcular a soma de uma lista de números.
    O programa deve dividir a lista em partes e atribuir cada parte a uma thread separada.
    Cada thread calcula a soma de sua parte da lista, e o programa principal agregará os
    resultados de todas as threads para obter a soma total.
    Realize comentários no código para explicar sua linha de raciocínio.
"""

from threading import Thread, Lock
import random

lock = Lock()
global_sum = 0
random_number_list = []

def SumList(number_list):
    global global_sum
    local_sum = 0
    # Faz a soma dos números
    for i in range(len(number_list)):
        local_sum += number_list[i]
    lock.acquire()
    # Adiciona na variável global dentro de um Lock para não gerar conflitos
    global_sum += local_sum
    print(f'Current sum in thread: {global_sum}')
    lock.release()

# Cria uma lista de tamanho 10 com números aleatórios de 1 a 10
for i in range(10):
    random_number_list.append(random.randint(1, 10))

first_half = random_number_list[:len(random_number_list)//2]
second_half = random_number_list[len(random_number_list)//2:]

print(random_number_list)
print(first_half)
print(second_half)

thread1 = Thread(target=SumList(first_half), args=())
thread2 = Thread(target=SumList(second_half), args=())

thread1.start()
thread2.start()

# Espera até que as duas threads sejam finalizadas para printar o resultado final
thread1.join()
thread2.join()
print(f'Final sum: {global_sum}')