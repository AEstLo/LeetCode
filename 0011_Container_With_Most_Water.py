class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        result = min(height[l], height[r]) * (r - l)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
        while l < r:
            result = max(min(height[l], height[r]) * (r - l), result)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return result
