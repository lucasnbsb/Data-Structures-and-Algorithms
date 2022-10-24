class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes = {}
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes[nums[i]] = i
            else:
                if abs(dupes[nums[i]] - i) <= k:
                    return True
                else:
                    dupes[nums[i]] = i
        return False