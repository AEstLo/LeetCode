class Solution:
    def trap(self, height: List[int]) -> int:
        # Being N the number of elements
        # Time: O(N)
        # Space: O(N)
        N = len(height)
        max_from_left = [0] * N
        max_from_right = [0] * N

        current_max = 0
        for i, h in enumerate(height):
            max_from_left[i] = current_max
            if h > current_max:
                current_max = h

        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            max_from_right[i] = current_max
            if h > current_max:
                current_max = h

        total = 0
        for i, h in enumerate(height):
            if max_from_left[i] > h and max_from_right[i] > h:
                total += min(max_from_left[i], max_from_right[i]) - h
        return total
