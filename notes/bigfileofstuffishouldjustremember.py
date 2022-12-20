from collections import deque
import numpy as np
# this is the big file of things i should just remember



# Quicksort:
def quicksort(arr, s, e):
    if (e-s +1) <= 1:
        return
    pivot = arr[e]
    left = s
    for i in range(s, e):
        if(arr[i] <= pivot):
            #Swap with left
            arr[i], arr[left]  = arr[left], arr[i]
            left+= 1
    #Stap pivot with the middle
    arr[e] , arr[left] = arr[left], arr[e]
    quicksort(arr, s, left-1) # the middle one is alredy in order
    quicksort(arr, left+1, e)
    return arr

# Binary Search:
def binarySearch(a, target):
    left, right  = 0, len(a)-1
    while left<= right:
        mid = (left+right)//2
        if target > a[mid] : left = mid+1
        elif target < a[mid] : right = mid-1
        else: return mid
    return -1

# Binary search generalized for minimalizing X such that f(x) is the minimum
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    left, right = 0, len(array)
    while left < right:
        mid = left + ((right - left)>>1)
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# BSF:
def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

# DSF:
    def dfs(root):
        if not root:
            return
        # stop condition
        # early killswitches
        dfs(root.left)
        dfs(root.right)


def binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    left, right = 0, len(array)
    while left < right:
        mid = left + ((right - left)>>1)
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# generalized algorithm is for finding minimum number k in a search space such that a condition holds
# apply when some form of monotonicity is found within the search space.

# left is the minimun number s.t condition = true.
# left-1 is the maximun number s.t condition = false.


#Union Find 

class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        #graphs with node marked 1 to n
        for i in ranger(1, n+1):
            self.parents[i] = i
            self.rank[i] = 0

    def find(self, n):
        par = self.parents[n]
        while par != self.parents[par]:
            #path compression
            self.parents[par] = self.parents[self.parents[par]]
            par = self.parents[par]
        return par
    
    def union(self, n, m):
        p1, p2 = self.find(n), self.find(m)

        if p1 == p2: return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.rank[p2] += 1
        return True 

# Kruskal's -> minimun spannign tree
    # joga tudo num minheap
    # vai tirando do heap até que arestas = nodos-1
    # se union(i,j) == false continue
    # se nao poe na msp

# Kadane:
    cur = max(cur+n, n)
    max =max(cur, max)


