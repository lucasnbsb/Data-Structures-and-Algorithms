class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(nums, target, index, path) -> bool:
            if target < 0: 
                return True
            if target == 0: 
                res.append(path)
                return True
            #same trick as last time, this makes it so that only one execution
            #of a repeated digit goes through to the recursive part
            for i in range(index, len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                dfs(nums, target-nums[i], i+1, path + [nums[i]])     
        dfs(candidates, target, 0, [])
        return(res)
    