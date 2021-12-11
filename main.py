import threading
import time
import random

n = 110
k1 = 20
k2 = 5
t= 3

buffer = [0 for i in range(n)]

def produce(next_in):
    
    while 1:
        for i in range(k1):
            buffer[(next_in + i) % n] += 1
        next_in = (next_in + k1) % n
        t1 = random.randint(0, t)
        time.sleep(t1)
        

def consume(next_out):
    
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
        

next_in = 0
next_out = 0
t1 = threading.Thread(target = produce, args=[next_in])
t2 = threading.Thread(target = consume, args=[next_out])

t1.start()
t2.start()
