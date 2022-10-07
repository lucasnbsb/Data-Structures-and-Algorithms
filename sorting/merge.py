from cmath import log
from tempfile import tempdir
import numpy as np


def mergeSort(arr, s, e):
    # when the array is 1 element long its sorted
    if e-s+1 <= 1:
        return arr

    # when its not divide in 2, sort and merge
    m = (e+s)//2  # integer division, rounds down

    # sort first half
    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)

    merge(arr, s, m, e)
    return arr


def merge(arr, s, m, e):
    L = arr[s:m+1] # little peculiarity with the indexes here
    R = arr[m+1:e+1] 

    i = 0  # index for left
    j = 0  # index for right
    k = s  # index for result array

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # passa o que sobrar no final
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


a = np.random.randint(0, 100, 50)
print(mergeSort(a, 0, len(a)))
