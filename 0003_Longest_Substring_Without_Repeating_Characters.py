class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Let us use a sliding window and a set
        # Being n the length of s
        # Time: O(n)
        # Space: O(n)
        left = 0
        right = 0
        current_chars = set()

        longestSubstring = 0
        N = len(s)
        while right < N:
            while right < N and s[right] not in current_chars:
                current_chars.add(s[right])
                right += 1
            longestSubstring = max(longestSubstring, len(current_chars))
            while right < N and s[left] != s[right]:
                current_chars.remove(s[left])
                left += 1
            current_chars.remove(s[left])
            left += 1
        return longestSubstring
