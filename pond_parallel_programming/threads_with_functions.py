from threading import Thread, Lock
import time

money = 0
lock = Lock()

def updateMoney():
    global money
    lock.acquire() # bloqueia outras threads de acessarem o recurso que a thread atual está acessando 
    value = money
    time.sleep(.001)
    money = value + 10
    lock.release()

# create threads
threads = []

for i in range(20):
    threads.append(Thread(target=updateMoney, args=()))

# start the threads 
for i in range(20):
    threads[i].start()

# join the threads
for i in range(20):
    threads[i].join()