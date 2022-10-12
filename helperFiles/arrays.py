from collections import deque
from typing import List

def canFormTriangle(nums):
    return ((nums[0]+nums[1])>nums[2] and (nums[2]+nums[1])>nums[1] and (nums[0]+nums[2])>nums[1])

def findLargestTriangle(nums):
    first = 0
    second = 0
    third = 0
    for num in nums:
        if num >= first:
            if(first >= second):
                second = first
                if(second >= third):
                    third = second
            first = num
        elif num >= second:
            if(second >= third):
                third = second
            second = num
        elif num >= third:
            third = num
    return [first, second, third]
        

def largestPerimeter(nums: List[int]) -> int:
    largest = findLargestTriangle(nums)
    return sum(largest) if canFormTriangle(largest) else 0

def canFormTriangle(nums):
    return ((nums[0]+nums[1])>nums[2] and (nums[2]+nums[1])>nums[1] and (nums[0]+nums[2])>nums[1])

if __name__ == '__main__':
    nums = [2,1,3,50,7,9,1,2,1,90,8,8,7]
    nums.sort()
    
    for i in range(len(nums)-1, 1, -1):
        (nums[i], nums[i-1], nums[i-2])

    print(canFormTriangle([90,50,9]))
