#SETS
myset = set()
myset = {1,2,3}
myset.add(4)
myset.remove(2)
for x in myset: print(set)

#Hashmap
from collections import defaultdict
myDict = collections.defaultdict(int | str | float| list)
dict.keys() - dict.values() - dict.copy()
hash(string)

# Array
a[::-1] # reverse

# transformar um array em string
''.join(currentString)

# iterar de trás pra frente
for a in range(len(array)-1 , -1, -1 ):
for a in arr[::-1]
for a in reversed(arr)

# Checking all neighbors in matrix
for x in range(r-1, r+2):
    for y in range(c-1, c+2):
        if (x >= 0 and x < ROWS and
            y >= 0 and y < COLS and
            not (x==r and y==c):
                #do something

# checking diagonals and antidiagonals
x - y = p - q # antidiagonals
x + y = p + q # diagonals

# Sorting:
arr.sort(key = lambda i: i[0])
arr.sort(reverse = True)
arr.sort()

# Heaps
import heapq
minHeap = []
heapq.heappush(minHeap, [index, whatever, else_])
heapq.heappop()

#List Comprehension
grid = [[1]*n for _ in range(m)]

