import math
import numpy as np
import threading

iterations_count = round(1e7)

def threadIt(start, stop):
   for j in range(start, stop):
        [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]
        print("Complex operation. Input index: " + str(j))
        #[math.exp(i) * math.sinh(i) for i in [1] * iterations_count]
      
def runIt():
    for n in range(0, 10):
        stop = n + 1
        current = stop
        print("I'm thread #" + str(current))
        threading.Thread(target = threadIt, args= (n,stop)).start()

runIt()