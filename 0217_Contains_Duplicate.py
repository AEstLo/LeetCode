class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(N)
        # Space: O(N)
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

# Runtime: 872 ms, faster than 16.48% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 30.90% of Python3 online submissions for Contains Duplicate.
