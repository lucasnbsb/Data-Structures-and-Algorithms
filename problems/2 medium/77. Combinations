class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = range(1,n+1)
        def backtrack(path, k , index):
            if k == 0:
                res.append(path)
                return
            for i in range(index, len(nums)):
                backtrack(path+[nums[i]], k-1, i+1)
                
        backtrack([], k, 0)
        return res