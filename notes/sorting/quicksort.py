import numpy as np

def quicksort(arr, s, e):
    if (e-s +1) <= 1:
        return
    pivot = arr[e]
    left = s

    for i in range(s, e):
        if(arr[i] <= pivot):
            #swap with left
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left+= 1

    #move pivot
    arr[e] = arr[left]
    arr[left] = pivot

    quicksort(arr, s, left-1) # the middle one is alredy in order
    quicksort(arr, left+1, e)

    return arr

a = np.random.randint(0, 100, 50)
print(quicksort(a, 0, len(a)-1))