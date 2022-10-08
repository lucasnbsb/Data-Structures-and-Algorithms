from socket import J1939_MAX_UNICAST_ADDR


class Solution:
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        
        def quickselect(s,e):
            pivot, left = nums[e], s
            for i in range(s, e):
                if(nums[i] <= pivot):
                    nums[i],nums[left] = nums[left],nums[i]
                    left += 1
            nums[left], nums[e] = nums[e], nums[left]        

            if left > k: return quickselect(s, left-1)
            elif left < k: return quickselect(left+1, e)
            else: return nums[left]
        
        return quickselect(0, len(nums) -1)



