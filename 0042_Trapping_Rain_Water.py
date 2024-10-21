class Solution:
    def trap(self, height: List[int]) -> int:
        # Being N the number of elements
        # Time: O(N)
        # Space: O(1)
        l = 0
        n = len(height)
        while l < n - 1 and height[l] < height[l + 1]:
            l += 1
        r = l + 1
        result = 0
        while r < n:
            while r < n and height[l] > height[r]:
                r += 1
            if r < n:
                min_height = min(height[l], height[r])
                l += 1
                while l < r:
                    result += min_height - height[l]
                    l += 1
                r += 1

        peak = l
        r = n - 1
        while r > 0 and height[r] < height[r - 1]:
            r -= 1
        l = r - 1
        while l >= peak:
            while l >= 0 and height[r] > height[l]:
                l -= 1
            if l >= 0:
                min_height = min(height[l], height[r])
                r -= 1
                while l < r:
                    result += min_height - height[r]
                    r -= 1
                l -= 1

        return result
