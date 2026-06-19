class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0
        l = 0
        r = len(height) - 1

        while l < r:
            output = max(min(height[l],height[r]) * (r - l), output)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return output
