class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        maxArea = 0

        while l < r:
            minHeight = min(height[l], height[r])
            currentArea = minHeight * (r - l)
            maxArea = max(maxArea, currentArea)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1

        return maxArea