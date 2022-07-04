class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        h = 1
        while h < x:
            h *= 10
        h /= 10
        while x >= 10:
            d = x // h
            m = x % 10
            if d != m:
                return False
            x %= h
            x //= 10
            h //= 100

        return True if x== 0 or h <= 1 else False
