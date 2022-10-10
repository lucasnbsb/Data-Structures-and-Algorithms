# two pointers one from the beguining swaping zeroes and one from the end swaping 2s
# pay attention to the edge case of the two swap for a zero, thats why we dont
# increment i on that case
# why is it this much faster to swap like this?
class Solution:
    def sortColors(self, nums: List[int]) -> None:
    
        i, l,r = 0,0, len(nums)-1
        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
                r -= 1
                i -=1
            i+=1    
            