import threading
import time

class MyThread(threading.Thread):
    
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message
    
    def run(self):
        while(True):
            print(self.message)
            time.sleep(1)


thread1 = MyThread("Thread 1")
thread2 = MyThread("Thread 2")
thread3 = MyThread("Thread 3")
thread4 = MyThread("Thread 4")

thread1.start()
# thread1.join()

thread2.start()
# thread2.join()

thread3.start()
# thread3.join()

thread4.start()
# thread4.join()

"""
    Other threads can call a thread’s join() method.
    This blocks the calling thread until the thread
    whose join() method is called is terminated.
    From: https://docs.python.org/3/library/threading.html
"""