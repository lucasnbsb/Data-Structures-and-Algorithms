from tempfile import tempdir
import numpy as np

nums = np.random.randint(0, 100, 50)
# O(n^2)
for i in range(1, len(nums)):
    j = i-1
    while( j >= 0 and nums[j+1] < nums[j]):
        temp = nums[j+1]
        nums[j+1] = nums[j]
        nums[j] = temp
        j -= 1
print(nums)