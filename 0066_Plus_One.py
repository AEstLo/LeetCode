class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time:  O(N)
        # Space: O(1)
        N = len(digits)
        i = N - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits

# Runtime: 35 ms, faster than 90.44% of Python3 online submissions for Plus One.
# Memory Usage: 14 MB, less than 11.12% of Python3 online submissions for Plus One.
