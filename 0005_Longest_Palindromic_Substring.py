class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Being n the length of s
        # Time: O(n^2)
        # Space: O(n)
        if not s:
            return ''
        N = len(s)
        if N == 1:
            return s[0]
        maxLength = 0
        result = ''
        for i in range(N):
            # Checking the odd cases
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                if maxLength < r - l + 1:
                    maxLength = r - l + 1
                    result = s[l:r + 1]
                l -= 1
                r += 1

            # Checking the even cases
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if maxLength < r - l + 1:
                    maxLength = r - l + 1
                    result = s[l:r + 1]
                l -= 1
                r += 1
        return result
