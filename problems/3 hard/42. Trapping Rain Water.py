class Solution(object):
    def trap(self, height):
        maxHeightFromTheLeft = []
        maxLeft = 0
        for h in height:
            maxLeft = max(h, maxLeft)
            maxHeightFromTheLeft.append(maxLeft)
        
        maxRight = 0
        for i, h in reversed(list(enumerate(height))):
            maxRight = max(h, maxRight)
            maxHeightFromTheLeft[i] = min(maxRight, maxHeightFromTheLeft[i]) - h
        return sum(maxHeightFromTheLeft)
