class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        maxArea = 0

        left = 0
        right = n - 1

        while left < right:
            h = min(height[left], height[right])
            length = right - left
            area = h * length
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea