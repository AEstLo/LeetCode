class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)
        total = 0
        for num in nums:
            total ^= num
        return total

# Runtime: 179 ms, faster than 72.68% of Python3 online submissions for Single Number.
# Memory Usage: 16.9 MB, less than 20.31% of Python3 online submissions for Single Number.
