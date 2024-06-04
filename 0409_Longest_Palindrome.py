class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        longest = 0
        for char in s:
            if char in seen:
                seen.remove(char)
                longest += 2
            else:
                seen.add(char)
        if seen:
            longest += 1
        return longest
