class Solution:
    def isPalindrome(self, s: str) -> bool:
        ord_a = ord('a')
        ord_z = ord('z')
        ord_zero = ord('0')
        ord_nine = ord('9')
        def isAlpha(char):
            return (
                (ord_a <= ord(char) <= ord_z)
                or
                (ord_zero <= ord(char) <= ord_nine)
            )

        l, r = 0, len(s) - 1
        t = s.lower()
        while l < r:
            while l < r and not isAlpha(t[l]):
                l += 1
            while r > l and not isAlpha(t[r]):
                r -= 1
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True
