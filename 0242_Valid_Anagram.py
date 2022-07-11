class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Being S the number of characters of s and T the number of characters of T
        # Time: O(S + T)
        # Space: O(S + T)
        return collections.Counter(s) == collections.Counter(t)
