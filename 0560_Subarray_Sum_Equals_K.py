class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time: O(N)
        # Space: O(N)
        # Credits: https://www.youtube.com/watch?v=fFVZt-6sgyo
        total = 0
        helper_sum = {
            0: 1,
        }

        acum = 0
        for num in nums:
            acum += num
            diff = acum - k
            if diff in helper_sum:
                total += helper_sum[diff]
            if acum not in helper_sum:
                helper_sum[acum] = 0
            helper_sum[acum] += 1

        return total

# Runtime: 342 ms, faster than 77.86% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.5 MB, less than 97.99% of Python3 online submissions for Subarray Sum Equals K.
