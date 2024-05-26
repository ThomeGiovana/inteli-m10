from threading import Thread, Lock
import random

lock = Lock()
global_sum = 0
random_number_list = []
random_number_list_separations = []
n_threads = 5 # Aqui modificamos o número de threads que queremos que executem a soma
threads = []

def SumList(number_list):
    global global_sum
    local_sum = 0
    # Faz a soma dos números
    for i in range(len(number_list)):
        local_sum += number_list[i]
    lock.acquire()
    # Adiciona na variável global dentro de um Lock para não gerar conflitos
    global_sum += local_sum
    print('============================')
    print(f'Sublist in thread: {number_list}')
    print(f'Current sum in thread: {global_sum}')
    lock.release()

def SplitList(random_number_list, n_threads):
    # Calcula o tamanho das sublistas
    sublist_size = len(random_number_list) // n_threads
    remainder = len(random_number_list) % n_threads
    
    sublists = []
    start = 0
    
    for i in range(n_threads):
        # Calcula o tamanho da sublista atual
        end = start + sublist_size + (1 if i < remainder else 0)
        sublists.append(random_number_list[start:end])
        start = end
    
    return sublists

def CalculateGroundTruth(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum





# Cria uma lista de tamanho 100 com números aleatórios de 1 a 100
for i in range(100):
    random_number_list.append(random.randint(1, 100))
# Separa as listas
random_number_sublists = SplitList(random_number_list, n_threads)

print(random_number_list)
for i in range(n_threads):
    threads.append(Thread(target=SumList(random_number_sublists[i]), args=()))

for i in range(n_threads):
    threads[i].start()

# Espera até que as duas threads sejam finalizadas para printar o resultado final
for i in range(n_threads):
    threads[i].join()
print(f'===== Final sum: {global_sum} =====\n===== Ground truth: {CalculateGroundTruth(random_number_list)} =====')
