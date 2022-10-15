from collections import deque
from typing import List
from numpy import empty

if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    target = 7
    res = []

    arr = [1]
    for i in range(len(arr)):
        a = arr[0:i] + arr[i+1:]
        print(a)