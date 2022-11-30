class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [1]*n
        
        tmpPre = 1
        for i in range(n):
            out[i] = tmpPre
            tmpPre *= nums[i]
            
        
        tmpPost = 1
        for i in range(n-1, -1, -1):
            out[i] *= tmpPost
            tmpPost *= nums[i]
        
        return out
            
            
                    