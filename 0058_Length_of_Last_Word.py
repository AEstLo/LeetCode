class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Time: O(N)
        # Space: O(1)
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        total = 0
        while i >= 0 and s[i] != ' ':
            total += 1
            i -= 1
        return total

# Runtime: 51 ms, faster than 36.30% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.9 MB, less than 79.68% of Python3 online submissions for Length of Last Word.
