class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        max_sequence = 0
        for num in s:
            if num - 1 not in s:
                i = num + 1
                cur = 1
                while i in s:
                    i += 1
                    cur += 1
                max_sequence = max(max_sequence, cur)
        return max_sequence
