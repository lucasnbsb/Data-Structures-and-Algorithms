class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calcArea(l, r):
            return min(height[l], height[r]) * (r-l)
        left = 0
        right = len(height)-1
        maxarea = 0
        while left < right:
            tmp = calcArea(left, right)
            maxarea = max(maxarea, tmp)
            if height[left] > height[right]:
                right -=1
            else:
                left += 1
        return maxarea