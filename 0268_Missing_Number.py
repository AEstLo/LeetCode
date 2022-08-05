class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
        return -1

# Runtime: 4740 ms, faster than 5.01% of Python3 online submissions for Missing Number.
# Memory Usage: 15.7 MB, less than 9.90% of Python3 online submissions for Missing Number.
