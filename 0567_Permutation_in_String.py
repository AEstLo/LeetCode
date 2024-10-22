class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        set_s1 = collections.Counter(s1)
        len_s1 = len(s1)
        s = collections.Counter(s2[0:len_s1])
        for i in range(len_s1, len(s2)):
            if set_s1 <= s:
                return True
            s[s2[i - len_s1]] -= 1
            s[s2[i]] += 1
        return set_s1 <= s
