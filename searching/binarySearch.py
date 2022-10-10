import numpy as np


def binarySearch(a, target):
    l, r  = 0, len(a)-1

    while l<= r:
        mid = (l+r)//2
        if target > a[mid] :
            l = mid+1
        elif target < a[mid] :
            r = mid-1
        else:
            return mid
    return -1

a = np.random.randint(0, 100, 50)
a.sort()
target = a[10]
print(binarySearch(a, target))zz