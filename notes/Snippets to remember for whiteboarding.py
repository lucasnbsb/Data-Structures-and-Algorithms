
# Linked list node
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Tree node -> notice its the same thing
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#SETS
myset = set()
myset = {1,2,3}
myset.add(4)
myset.remove(2)
for x in myset: print(set)

#Hashmap
from collections import defaultdict
default_value = 0
mydefaultDict = defaultdict(default_value)
wordsDict = defaultdict(int) # tudo em zero
dict.keys()
dict.values()
dict.copy()
hash(string)

# Array
a[::-1] # reverse

# transformar um array em string
''.join(currentString)

# iterar de trás pra frente
for a in range(len(array), -1, -1 ):

# (x//3, y//3) - addressing squares in sudoku

myhashmap = {}
myhashmap[i] = 0

# Checking neighbors

for x in range(r-1, r+2):
    for y in range(c-1, c+2):
        if (x >= 0 and x < ROWS and
            y >= 0 and y < COLS and
            not (x==r and y==c):
                #do something