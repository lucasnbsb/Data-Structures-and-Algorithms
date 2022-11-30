#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    maxheap = []
    minheap = []
    
    def add(i):
        heapq.heappush(maxheap, -i)
        heapq.heappush(minheap, -heapq.heappop(maxheap))
        if len(minheap) > len(maxheap):
            heapq.heappush(maxheap, -heapq.heappop(minheap))
    
    def median(index):
        if len(maxheap) > len(minheap):
            return -maxheap[0]
        else:
            return (minheap[0]-maxheap[0]) / 2
        
    
    output = []
    for i in a:
        add(i)
        output.append(median(i))
    
    return output
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
