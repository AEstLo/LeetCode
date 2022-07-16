class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time:  O(N*H)
        # Space: O(1)
        if not needle:
            return 0
        # Let's suppose this function does not exist
        # return haystack.find(needle)
        H = len(haystack)
        N = len(needle)
        i = 0
        while i < H:
            if haystack[i] == needle[0]:
                n = 1
                h = i + 1
                while n < N and h < H:
                    if haystack[h] != needle[n]:
                        break
                    n += 1
                    h += 1
                if n == N:
                    return i
            i += 1

        return -1

# Runtime: 36 ms, faster than 82.04% of Python3 online submissions for Implement strStr().
# Memory Usage: 13.8 MB, less than 63.66% of Python3 online submissions for Implement strStr().
