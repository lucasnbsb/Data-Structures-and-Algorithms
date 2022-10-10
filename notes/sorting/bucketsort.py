import numpy as np

a = np.random.randint(0, 100, 50)

def bucketsort(a):
    values = [0]*100
    for i in a:
        values[i] += 1
    
    i = 0
    for n in range(0, len(values)):
        for i in range(0, values[n]):
            a[i] = n
            i+=1

    return a

print(bucketsort(a))