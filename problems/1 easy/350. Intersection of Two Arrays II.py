class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occ = {}        
        for num1 in nums1:
            if num1 not in occ:
                occ[num1] = 1
            else:
                occ[num1] += 1
        
        out = []
        for num2 in nums2:
            if num2 in occ and occ[num2] >= 1:
                out.append(num2)
                occ[num2] -= 1
        return out