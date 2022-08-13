class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        n = len(nums)

        more_than = n // 2
        for num in c:
            if c[num] > more_than:
                return num
        return -1

# Runtime: 156 ms, faster than 99.65% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 35.08% of Python3 online submissions for Majority Element.
