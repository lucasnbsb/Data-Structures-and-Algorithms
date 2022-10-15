class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        def back(path, k , arr):
            if k == 0:
                res.append(path)
                return
            for i in range(0, len(arr)):
                back(path+[arr[i]], k-1, arr[0:i] + arr[i+1:])
        back([], size, nums)
        return res