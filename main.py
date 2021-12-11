import threading
import time
import random

n = 110
k1 = 20
k2 = 5
t= 2
next_out = 0
next_in = 0
binar = threading.Semaphore(1)
buffer = [0 for i in range(n)]
def Produce(next_in): 
    binar.acquire()
    while 1:
        for i in range(k1):
            buffer[(next_in + i) % n] += 1
        next_in = (next_in + k1) % n
        t1 = random.randint(0, t)
        time.sleep(t1)
        binar.release()
def Consume(next_out):  
    binar.acquire()
    while 1:
        t2 = random.randint(0, t)
        time.sleep(t2)
        for i in range(k2):
            data = buffer[(next_out + i) % n]
            if data > 1:
                print("Race condition: \n")
                print(buffer)
                return
        next_out = (next_out + k2) % n
        binar.release()

Produce = threading.Thread(target = Produce, args=[next_in])
Consume = threading.Thread(target = Consume, args=[next_out])

Produce.start()
Consume.start()
